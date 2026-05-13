# Architecture


The diagram below shows the high-level architecture of the Contract Assistant Agent, including the presentation layer, application logic, scoring, data extraction, external dependencies, and data flow.

```mermaid
%%{init: {
  'flowchart': {
    'nodeSpacing': 160,
    'rankSpacing': 120,
    'curve': 'basis'
  },
  'themeVariables': {
    'fontSize': '16px'
  }
}}%%
graph TB

%% === STYLES ===
classDef core fill:#1E90FF,stroke:#000,color:#000,stroke-width:2px,rx:10px,ry:10px;
classDef data fill:#9ACD32,stroke:#000,color:#000,stroke-width:2px,rx:10px,ry:10px;
classDef external fill:#FFD700,stroke:#000,color:#000,stroke-width:2px,rx:10px,ry:10px;

%% === USER ===
User(("User<br/>Uploads Contract Document"))

%% === PRESENTATION LAYER ===
subgraph "Presentation Layer"
    App["app.py<br/>Streamlit UI"]:::core
end

User -->|uploads file| App

%% === APPLICATION LOGIC LAYER ===
subgraph "Application Logic Layer"
    Processor["processor.py<br/>Business Logic"]:::core
end

App -->|invokes analysis| Processor

%% === DATA MODELS LAYER ===
subgraph "Data Models Layer"
    Schema["schemas.py<br/>Data Models"]:::core
end

%% === SCORING LAYER ===
subgraph "Scoring Layer"
    Score["scoring.py<br/>Scoring Algorithms"]:::core
end

%% === DATA EXTRACTION LAYER ===
subgraph "Data Extraction Layer"
    Extract["parsers.py<br/>Data Extraction"]:::core
end

%% === TESTING LAYER ===
subgraph "Testing"
    Test["tests/<br/>Unit Tests"]:::core
end

%% === DATA FLOW ===
subgraph "Data Flow"
    TXT["Extracted Text<br/>from Contract"]:::data
    NORM["Normalized Text"]:::data
    MONEY["Monetary Value"]:::data
    DATE["Date Range"]:::data
    RES["Analysis Results<br/>Risk Score, Recommendations"]:::data
end

%% === EXTERNAL DEPENDENCIES (ALINHADAS COM A CAMADA DE DADOS) ===
subgraph "External Dependencies"
    DOCX["python-docx<br/>DOCX Parsing"]:::external
    PDF["pypdf<br/>PDF Text Extraction"]:::external
end

%% === RELATIONSHIPS ===
Processor -->|uses ContractAnalysisResult| Schema
Processor -->|calls score_contract| Score
Processor -->|calls extract_text| Extract

Extract -->|uses| DOCX
Extract -->|uses| PDF

Extract -->|returns extracted text| TXT
TXT -->|normalizes| NORM
NORM -->|parses monetary values| MONEY
NORM -->|parses dates| DATE

Processor -->|returns analysis results| RES

Test -->|ensures correctness| Processor
Test -->|ensures correctness| Score
Test -->|ensures correctness| Extract
```
