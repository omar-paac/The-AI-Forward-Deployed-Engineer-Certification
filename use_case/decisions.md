# Decision log

One row per architectural decision, with the option you rejected and why.

> **Week 5 asks you to defend your agent architecture against the alternatives.**
> **Week 10's handoff doc is largely this file.** Both are much easier if you
> wrote the reasoning down while you still remembered it.

A decision without a rejected alternative is not a decision, it is a default.
If you cannot name what you did not do, you did not choose.

| Week | Decision | What you rejected | Why | What would change your mind |
| --- | --- | --- | --- | --- |
| 1 | A function | Agentic process | (1 of 4) The ILS call is a fixed step. Even with thousands of part numbers and different conditions, a request would have the same shape; it isn't open-ended | If 1 of 5 requests get searched outside the ILS marketplace, the search depends on the part family, so it stops being fixed, and an agent might be helpful. I'd check the previous REQ or RFQs how they get solved |
| 1 | To match the Marketplace Account vs the SF Account, a custom field in Account object is needed 'ILS_Code__C'. We are going to do it once per vendor manual, (can be a script) fills up over time as buyers meet new vendors | I rejected comparing names, Rejected matching 'contacts' email domains | names differ a lot, something like "Aero Parts Inc" vs "AeroParts, Inc." will break at the domains, some vendor's use ILS or Gmail domains | If ILS decides to change those codes, it will break, so we will depend on their list. |
| 1 | After the buyer demo: the next slice is mass-sending RFQ emails and logging the RFQs, with a dropdown that merges ILS RFQ emails with our AvSight contacts | Building more vendor-search features first (e.g. checking OEM platforms) | All three buyers said emailing and recording RFQs is the most time-consuming job; ILS RFQ emails can't be tracked until a vendor replies | If timing a real pass showed vendor search takes longer than emailing and logging |
| 3 | <!-- --> | <!-- --> | <!-- --> | <!-- --> |
| 5 | <!-- agent architecture --> | <!-- --> | <!-- --> | <!-- --> |
| 6 | <!-- guardrail level --> | <!-- --> | <!-- --> | <!-- --> |
| 7 | <!-- memory type --> | <!-- --> | <!-- --> | <!-- --> |
| 8 | <!-- model --> | <!-- --> | <!-- --> | <!-- --> |

The case for an agent: If a Part number and condition is not found in the main market placed, this can be source in different marketplaces, however this depends on the part number family and where this is installed, so the agent could learn to identify this and point to the right vendor or OEM pages directly. We might point an agent to do a global research.

---

The last column is the one people skip and the one people ask about. "We chose
dense retrieval; we would switch to hybrid if exact-match queries went above ~20%
of traffic" is an engineering position. "We chose dense retrieval" is a
preference.
