# Project charter

<!--
  Fill this in during TC1 Step 4, from your Getting to Concreteness form.
  Later weeks' notebooks read this file and stop if it is still the template.
  That is on purpose.
-->

**Department:** Purchasing

**Working title:** Vendor Quotes Collector

---

## The problem

**Who has it?** One real role, not a department.

Purchasing Representatives, around 10 people in total.

**What are they trying to do?**

Sourcing part numbers in the open market to restock. Identify vendors, send emails, wait for responses, and follow up.

**How do they handle it today?**

Based on a purchase request, we source for the right vendor that matches our part number condition (New, New Surplus, Factory New) and Quantity. Once identified, we send an RFQ email, wait for the response, and log this into our ERP system. It takes around 5 min finding vendors, ~10 min emailing and logging the RFQs. Logging is slow because vendor info is typed in by hand.

**What does that cost — time, money, risk, or relationships?**

The purchasing representative spends 15 min total, most of it emailing and logging a part, at a ballpark estimate of $7 per part. Parts arriving late or not being available impact our customer service.

**The problem in one sentence. No solution in it.**

A slow part of getting material into stock is the 10 minutes manual emailing and logging process, the purchasing representative has to do before a PO is placed.

---

## Success

**What does the new world look like for that person?**

The person creates a Purchase Request and gets ranked vendors with each one's RFQ email and an ERP account already found, so less typing. Next an email draft and logging the RFQ in the ERP as next slice.

**How would the firm measure it? Which numbers should move?**

- A 50% time reduction in sending emails and logging RFQs in the system.
- A 30% increase in parts researched per week.

---

## The first product

**Your solution in one sentence.**

A system that will find the vendors for a part with their RFQ email and account, so sending and logging into the ERP take less time; drafting and logging come next.

**Input → Output.** Be specific enough that someone could build it wrong and you
would notice.

| | |
| --- | --- |
| **In** | Part Number, list of conditions, quantity, optional vendor cap |
| **Out** | A list of Vendor's listed part numbers with quantity and conditions, an RFQ email to reach out, an account ID or none, when the account is not mapped to the ERP system, and a reason why |
| **Out** | vendors exist, but every one is a near match, meaning short on quantity or an alternate part number offered |
| **Out** | No answer, when there are no vendors, and the reason |

---

## Decisions made later

<!--
  Amended as the cohort goes. Keep the reasoning, not just the choice — Week 5
  asks you to defend your architecture against the options you rejected, and
  Week 10's handoff doc is largely this section.
-->

| Week | Decision | Why, and what you rejected |
| --- | --- | --- |
| 3 | Retrieval approach | <!-- TC3 --> |
| 5 | Agent architecture | <!-- TC5 --> |
| 8 | Model | <!-- TC8 --> |
