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
