# One-Page Test Runbook

## Goal
Validate the demo quickly and keep tomorrow morning execution simple.

## Before you start
- Activate the Python environment.
- Confirm dependencies are installed.
- Make sure Streamlit launches.
- Keep one PDF and one DOCX sample ready.
- Use the mocked demo path, not a live integration path.

## Run order
1. Start the app.
2. Upload one sample contract.
3. Run parsing.
4. Run scoring and prioritization.
5. Run retrieval and recommendation.
6. Check the audit log.
7. Rehearse the full demo once.

## If something fails
- Start-up issue: restart the environment once.
- Upload issue: use the backup sample.
- Parsing issue: switch to the cleanest document.
- Output issue: rerun once and continue.

## Suggested launch
```bash
pytest -q
streamlit run app.py


## What to say if blocked
"The demo is mocked for repeatability, so I can switch to a backup sample and continue. The architecture and control flow remain the same in production."
