# Contract Assistant Agent

Streamlit app for contract analysis based on:
- contract value
- extracted dates
- days until expiration
- risk prioritization

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

- `app.py` — Streamlit interface
- `source/parsers.py` — text extraction and parsing
- `source/processor.py` — contract analysis logic