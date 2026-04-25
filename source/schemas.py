from dataclasses import dataclass
from typing import List

@dataclass
class ContractAnalysisResult:
    filename: str
    value: float
    start_date: str
    end_date: str
    days_to_expiry: int
    risk_score: int
    priority: str
    recommendation: str
    rationale: List[str]
    text_preview: str