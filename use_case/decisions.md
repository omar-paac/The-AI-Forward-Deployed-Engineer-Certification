# Decision log

One row per architectural decision, with the option you rejected and why.

> **Week 5 asks you to defend your agent architecture against the alternatives.**
> **Week 10's handoff doc is largely this file.** Both are much easier if you
> wrote the reasoning down while you still remembered it.

A decision without a rejected alternative is not a decision, it is a default.
If you cannot name what you did not do, you did not choose.

| Week | Decision | What you rejected | Why | What would change your mind |
| --- | --- | --- | --- | --- |
| 1 | A function | Agentic process | (1 of 4) The ILS call is a fixed step. Even with thousands of part numbers and different conditions, a request would have the same shape; it isn't open-ended | If 1 of 5 requestes get searched outside the ILS market place, the search depends on the part family, so it stops being fixed, and an agent might be helpful. I'd check the previous REQ or RFQs hotw they get solved |
| 1 | Too match the Marketplace Account vs the SF Account, a custom field in Account object is needed 'ILS_Code__C. We are going to do it once per vedor manuall, (can be an script) fills up over time as buyers meet new vendors | I rejectetd comparing names, Rejected matching 'contacts' email domains | names differ a lot, something like "Aero Parts Inc" vs "AeroParts, Inc." will break an the domaains, some vendor's use ils domain or gmail | If ILS decides to change those codes, it will break, so we will depend on their list. |
| 3 | <!-- --> | <!-- --> | <!-- --> | <!-- --> |
| 5 | <!-- agent architecture --> | <!-- --> | <!-- --> | <!-- --> |
| 6 | <!-- guardrail level --> | <!-- --> | <!-- --> | <!-- --> |
| 7 | <!-- memory type --> | <!-- --> | <!-- --> | <!-- --> |
| 8 | <!-- model --> | <!-- --> | <!-- --> | <!-- --> |

The case for an agent: If a Part number and condition is not found in the main market placed, this can be source in different market places, however this depends on the part number family and where this is installed, so the agent could learn to indentify this and point to the right vendor or OEM pages direclty. We might point an agent to do a global research.

---

The last column is the one people skip and the one people ask about. "We chose
dense retrieval; we would switch to hybrid if exact-match queries went above ~20%
of traffic" is an engineering position. "We chose dense retrieval" is a
preference.
