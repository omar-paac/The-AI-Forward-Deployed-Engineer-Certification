# TC1 — Vendor Quotes Collector

## Step 8 — The endpoint

### Answers

1. What is one thing you do at work this could take over? Searching and sorting vendors, with their RFQ email and account. The process of drafting emails and logging the RFQ in the system comes next.
2. What exactly goes in — a string, a file, several fields? Several fields: A Part Number, a list of conditions, quantity, and an option to cap the list of vendors to return.
3. What comes back, and who reads it? The purchasing representative. They will get a status (answered, low confidence or no answer). A ranked list of Vendors, with an email address, account ID and a reason per each vendor. The rep will be able to pick who to send the RFQ. The account ID will be used later, without it, we will not be able to log the RFQs in the system.
4. What did you name it, and why would an agent pick it correctly? find_rfq_vendors, the verb says the action, rfq_vendors says which vendors and for what, and the typed fields and docstring tell an agent what to send.

## Step 9 — Docker

### Answers

1. CDN dependency: The page depends on the CDN at runtime, so on a blocked network it would load but will do nothing. One solution would be to load it in the image at build, to serve it from the app.
2. Container image vs Venv: A virtual environment captures the Python packages, but still depends on the host's OS and other libraries, while a container image captures all that plus the command to run it as one artifact. That makes an image a version a team can deploy.  

## Step 11 — Vibe check

Name the aspect before looking at the response. Aspects: instruction-following, factual grounding, format adherence, reasoning, tone, refusal behaviour, handling of missing information.

### Pass 1 — General capability (the chat)

1. *Explain object-oriented programming in simple terms to a complete beginner.*
   - Aspect tested: Tone and factual grounding. How OOP is explained that a beginner can follow it.
   - Response: It used a Car analogy and a Dog analogy. Correct, a bit verbose, but it is clear in my opinion.
2. *Read a paragraph of your choosing and summarize the key points.*
   - Aspect tested: Factual grounding, keeping the key points and the numbers, and instruction following,really summarizing the answer.
   - Response: Kept every point, but it was about as long as the original; 5 bullets for 4 sentences and added an "Overall" line I didn't ask for.
3. *Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.*
   - Aspect tested: Instruction following.
   - Response: It did provide a 135 words story about a robot and a small sparrow, with an unexpected place, a "junkyard's forgotten corner". The story had an introduction, rising action and an end.
4. *If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to get exactly 12 apples and 9 oranges?*
   - Aspect tested: Reasoning.
   - Response: The answer was correct: 3 packs of apples and 3 packs of oranges. It showed the working, 12 ÷ 4 and 9 ÷ 3.

5. *Rewrite a paragraph of your choosing in a professional, formal tone.*
   - Aspect tested: Tone, is it more "formal"?
   - Response: It added a few more words, like "unsure" for "uncertain"; "test more" to "conduct additional testing" and changed the structure of the sentences to make it more formal.

Are the answers correct and useful? Yes in my opinion, but it tends to say more than asked.

### Pass 2 — My use case (the RFQ form)

1. Example button "Exact match": BACB30NW6K-5Y, NE, Qty. 150
   - Aspect tested: Exact Match. Right status and instructions following
   - Result: Yes, answered the right "Vendor A, 150 in NE, account 001FAKE0000000001."
2. Example button "Alternate PN": 69494J155, NS, Qty. 2
   - Aspect tested: An edge case, providing an alternate part number to the requested.
   - Result: Yes, low_confidence, Vendor C lists 69494J155-ALT., reason says to verify interchangeability.
3. Example button "Exact + unmapped": MS15001-3, NE + NS, Qt.y 10
   - Aspect tested: Handling missing information, the vendor is not mapped
   - Result: It does show the "Unmapped" account clearly. "Answered, Vendor C ranked first (exact), then Vendor E short at 4 of 10 and shown as Unmapped."

Does it behave the way I expected? Why or why not? Yes, because solve() is plain code, not an LLM yet, so we received the output as it is programmed to do.

### Pass 3 — Where it falls down

1. A real part number that is not in the fake data:
   - Aspect tested: Missing information
   - Result: The current answer matches what we have in the fake data "No answer. No vendor lists ASNA2386-05-06 in NS." however this needs to be tested once the ILS is connected and NO real vendor exist.
2. The part number in lowercase, or with spaces:
   - Aspect: Different Input handling
   - Result: "ms15001 3" instead of "MS15001-3" in the data, it still provides the right answer, with the two vendor in the fake data.
3. MS15001-3, NE + NS, qty 10, max vendors 1:
   - Aspect tested: Instructions following
   - Result: The fake data contains two vendors, one an exact match and the other unmapped, it did show only the correct one, however we are missing the non match Vendor, so the buyer might have more options to check.

Real limitations of this application:

1. No live ILS data connected, only fake listing.
2. ILS quantity field is not always numbers ("MFG", "M-REP"), we will have to test/program it against that.
3. No email draft or RFQ logging yet, which is the real time-consuming part we are trying to solve.

What a vibe check is worth as evidence, and one thing I would add before comparing two versions of the app: A vibe check is my opinion on one run; to compare two versions I'd use the 5 goldens and the script that checks status and vendors.

## Step 13 — Bring it to work

### Napkin math

Each number marked **measured** or **looked up**.

| Line | Value | Source |
| --- | --- | --- |
| Tokens per call | 0 in, 0 out: `find_rfq_vendors` makes no model call | measured |
| Cost per call | $0 in tokens | measured |
| Calls per day | 100 (example: 10 reps x 10 parts each) | example figure, not Pac-Air data |
| Model per year | $0 x calls per day x 250 = $0 | measured |
| Minutes per manual pass | 15 (5 finding vendors, 10 emailing and logging) | my estimate only |
| Loaded $/hour | $30 | example figure, not Pac-Air data |
| Human per year | 15 / 60 x $30 x 100 calls per day x 250 = $187,500 | calculated from the example figures |
| Ratio | Not meaningful: the model cost is $0. The real costs are hosting and the next slice | |

This slice saves the ~5 minutes of finding vendors: about $62,500 a year of that time. The 10 minutes of emailing and logging, about $125,000 a year, is what the next slice targets.

The next slice (drafting the RFQ email) will use a model, so it will have a real token cost. That is where this math matters.

### Latency

- Observed by hand: under 0.5 seconds per search (not a measured p95; 10 calls, local, fake data)
- My p95 target: under 30sec
- Cost or latency, which is more likely to stop it being used: Latency: the model cost is $0, so the risk is the live ILS call making the search slow.

### What I would swap

1. Data: The live ILS SOAP search, and AvSight accounts with ILS_Code__c.
2. Model or endpoint: We hold no LLM endpoint now, so an approved provider or a gateway, which my Director of Technology would have to sign off.
3. Access or approval: ILS API credentials for production, the new ILS_Code__c field in AvSight, and Director of Technology approval to deploy.

### Which project at work this is for

The RFQ Module in AvSight, on the REQ record.
