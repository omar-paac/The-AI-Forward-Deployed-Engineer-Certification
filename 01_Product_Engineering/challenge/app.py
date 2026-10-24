"""The server.

`gradio.Server` is a FastAPI app with Gradio's API engine bolted in. You get
queueing, streaming, and MCP for free, but you bring your own frontend. That
split is the point: the API is the product, the UI is disposable.
"""

import os
from pathlib import Path

from fastapi.responses import HTMLResponse
from gradio import Server

from llm import stream_reply
from schema import Request, solve

app = Server()

FRONTEND = Path(__file__).parent / "frontend" / "index.html"


# --- The API -----------------------------------------------------------------
# The `-> str` return annotation is REQUIRED. Without it Gradio infers zero
# output components and silently returns nothing. Ask us how we know.


@app.api(name="chat")
def chat(message: str, history: list | None = None) -> str:
    """Stream a reply to one user message."""
    yield from stream_reply(message, history)


@app.api(name="find_rfq_vendors")
def find_rfq_vendors(part_number: str, conditions: list[str], quantity: int, max_vendors: int = 5) -> str:
    """Find the ILS vendors worth sending an RFQ to for one part number.

    Searches ILS for the part (and its alternates) in the given condition codes
    (NE, NS, FN, OH, SV, AR), then ranks exact matches before vendors that are
    short on quantity or list an alternate part number. Each vendor carries its
    RFQ email and AvSight account ID (null when not mapped yet). Returns the
    Response as JSON: status answered, low_confidence, or no_answer.
    """
    request = Request(part_number=part_number, conditions=conditions, quantity=quantity, max_vendors=max_vendors)
    return solve(request).model_dump_json(indent=2)


# --- The frontend ------------------------------------------------------------
# Defining a route at "/" replaces Gradio's default UI with ours.


@app.get("/", response_class=HTMLResponse)
def homepage() -> str:
    return FRONTEND.read_text(encoding="utf-8")


@app.get("/health")
def health() -> dict:
    """Your future ops team will thank you. Load balancers need this."""
    return {"status": "ok", "model": os.getenv("LLM_MODEL", "gpt-4.1-mini")}


if __name__ == "__main__":
    # 0.0.0.0 so the container is reachable from the host. On your laptop this
    # is fine. On a firm network, "reachable from where, exactly?" is the
    # question this challenge wants you to go ask.
    #
    # Read the port rather than hardcoding it, so a machine that already has
    # something on 7860 can move this one without editing code.
    port = int(os.getenv("GRADIO_SERVER_PORT", "7860"))

    # Gradio announces the address it BOUND to, which is 0.0.0.0 -- not an
    # address a browser can open. Windows rejects it outright; macOS and Linux
    # quietly redirect it to localhost, which is why it looks fine on some
    # machines and broken on others. Print the one that always works.
    print(f"\n  Open http://localhost:{port} in your browser\n", flush=True)
    app.launch(server_name="0.0.0.0", server_port=port)
