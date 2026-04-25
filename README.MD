# Contract Assistant Agent

Aplicação demo em Streamlit para análise de contratos em `.pdf` e `.docx`.

## Estrutura

- `app.py`: interface Streamlit
- `src/parsers.py`: leitura e parsing de contratos
- `src/scoring.py`: lógica de score e recomendação
- `src/processor.py`: orquestração do fluxo
- `src/schemas.py`: estrutura dos resultados
- `samples/`: contratos de exemplo

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```