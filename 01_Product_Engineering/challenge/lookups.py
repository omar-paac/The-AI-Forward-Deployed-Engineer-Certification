"""Where solve() gets its data.

Two lookups, each reading a JSON file of fake data. In production the same two
functions call ILS SOAP and Salesforce instead; solve() should not change.
"""

import json
import re
from pathlib import Path

DATA = Path(__file__).parent / "data"


def normalize_pn(part_number: str) -> str:
    """Compare part numbers on letters and digits only: "69494J155." == "69494-J155"."""
    return re.sub(r"[^A-Z0-9]", "", part_number.upper())


def find_listings(part_number: str, conditions: list[str]) -> list[dict]:
    """Every ILS listing for this part number in one of these conditions, any quantity.

    Mirrors the ILS condition filter, and only retunrs parts foudn in those condition/s.
    Like ILS, a listing also comes back when the searched PN is its alternate: then
    listing["part_number"] is what the vendor lists, and listing["alt_part_number"] is ours.
    Solve() will pick which ones match the request.
    """
    listings = json.loads((DATA / "ils_listings.json").read_text(encoding="utf-8"))
    wanted = normalize_pn(part_number)
    return [
        listing
        for listing in listings
        if wanted in (normalize_pn(listing["part_number"]), normalize_pn(listing["alt_part_number"] or ""))
        and listing["condition"] in conditions
    ]


def match_account(ils_code: str) -> dict | None:
    """Our Salesforce account and contacts for an ILS vendor, or None if it is not mapped yet."""
    accounts = json.loads((DATA / "accounts.json").read_text(encoding="utf-8"))
    return next((account for account in accounts if account["ils_code"] == ils_code), None)
