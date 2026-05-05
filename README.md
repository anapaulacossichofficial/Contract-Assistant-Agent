# Contract Assistant Agent Demo

This repository contains a Streamlit-based demo for agentic contract renegotiation. The current presentation and demo flow are optimized for an interview setting, with a mocked execution path for repeatability and a Boto3-based control plane for orchestration.

## What this repo demonstrates

- A supervisor-led multi-agent architecture for contract renegotiation.
- AWS SDK for Python (Boto3) as the control-plane binding to Bedrock.
- A local Streamlit demo that can be run safely without production dependencies.
- A scoring, retrieval, and recommendation pipeline for contract review.
- Security and governance concepts such as least privilege, workload identity, and auditability.

## Current demo structure

Recommended entry points:
- `app.py` — Streamlit frontend.
- `src/parsers.py` — contract parsing logic for PDF and DOCX.
- `src/scoring.py` — scoring and prioritization.
- `src/schemas.py` — structured output model.
- `src/processor.py` — workflow orchestration.

Expected flow:
1. Upload contract documents.
2. Parse text, values, and dates.
3. Score and prioritize items.
4. Retrieve supporting context.
5. Generate recommendations and a renegotiation draft.
6. Review the audit log and final output.

## Environment setup

### Python
Use Python 3.11 or newer.

### Recommended packages
Typical runtime dependencies should include:
- `streamlit`
- `boto3`
- `python-dotenv`
- `pydantic`
- `pandas`
- `python-docx`
- `pdfplumber` or `pypdf`
- `watchdog`

If the repo already has a `requirements.txt`, install from that file first.

### Suggested install flow
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Running the demo

### Local launch
```bash
pytest -q
streamlit run app.py
```

### Best demo mode
For the interview, use the mocked path and a small, clean sample contract so the flow is fast and predictable.

## Improving the repo

### 1. Add a proper README structure
Include these sections:
- Overview
- Architecture
- Environment setup
- How to run
- Test strategy
- Troubleshooting
- Demo tips

### 2. Add a `.env.example`
Document any configuration values such as:
- AWS region
- Bedrock model IDs
- Mock mode flag
- Log level

### 3. Add a `Makefile` or helper script
Useful commands:
- `make setup`
- `make run`
- `make test`
- `make lint`
- `make demo`

### 4. Create a `tests/` directory
Recommended test templates:
- parser tests
- scoring tests
- schema validation tests
- end-to-end smoke test
- mock demo regression test

### 5. Add logging and observability
Make the demo easier to explain by logging:
- file upload
- parse success or failure
- scoring result
- routing decision
- final output

### 6. Add sample data
Keep one clean PDF and one DOCX under `samples/` for rehearsal.

### 7. Make mock vs live mode explicit
Add a toggle in the app or config:
- `MOCK_MODE=true` for demo rehearsal
- `MOCK_MODE=false` for a live integration path

### 8. Add a `scripts/` folder
Helpful scripts:
- `scripts/run_demo.sh`
- `scripts/run_tests.sh`
- `scripts/check_env.sh`

## Demo experience tips

- Keep one click path from upload to recommendation.
- Show a visible progress state during parsing and scoring.
- Make the audit trail obvious in the UI.
- Prefer a single sample scenario rather than switching datasets live.
- Have a backup file ready in case one document fails.

## Suggested next improvements

- Add a landing page that explains the business problem in one sentence.
- Add a sample output page with expected contract ranking.
- Add an architecture diagram image in the repo.
- Add a short FAQ for interview questions.
- Add a one-command demo launcher for tomorrow morning.

## Troubleshooting

- If the app does not start, verify the virtual environment and dependencies.
- If parsing fails, test with a smaller document first.
- If the output is incomplete, rerun using the mocked path.
- If the UI is slow, reduce logging noise and use smaller sample files.

## Demo message

When asked about the implementation, describe it as a mocked, repeatable local demo that mirrors the production control-plane design, while keeping the environment safe and predictable for interview use.
