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

Based on a purchase request, we source for the right vendor that matches our part number condition (New, New Surplus, Factory New) and Quantity. Once identified, we send an RFQ email, wait for the response, and log this into our ERP system.  

**What does that cost — time, money, risk, or relationships?**

The purchasing representative spends ~15min in researching a part, in different ways, that costs a ball park estimate of $7 per part. Parts reaching later or not been available impact our customer service.

**The problem in one sentence. No solution in it.**

A slow part of getting material into stock is the 15 minutes manual quoting process the purchasing representative has to do before a PO is placed.

---

## Success

**What does the new world look like for that person?**

The person Purchase Request and gets a notification once a Vendor RFQ is received for her/his evaluation.

**How would the firm measure it? Which numbers should move?**

- A 20% increase on Part Numbers researched (REQ) per week.
- A 10% increase on the opportunistic inventory.

---

## The first product

**Your solution in one sentence.**

A system that will help us research an specific part number in the open market, that will match the vendor, quantity and condition so we can proceed with an RFQ or a PO creation.

**Input → Output.** Be specific enough that someone could build it wrong and you
would notice.

| | |
| --- | --- |
| **In** | Part Number, Condition, Quantity |
| **Out** | A ranked list of vendors whose ILS listing matches, each with the PN, condition and quantity they list and a one-sentence reason |
| **Out** | vendors exist, but every one is a near match, meaning short on quantity or a different condition |
| **Out** | No answer, with the reason when no listing matches |

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
