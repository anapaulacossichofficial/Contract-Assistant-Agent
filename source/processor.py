from .parsers import extract_text, normalize_text, parse_money, parse_dates
from .scoring import calculate_days_to_expiry, score_contract
from .schemas import ContractAnalysisResult

def analyze_file(uploaded_file) -> ContractAnalysisResult:
    raw_text = extract_text(uploaded_file)
    normalized_text = normalize_text(raw_text)

    value = parse_money(normalized_text)
    start_date, end_date = parse_dates(normalized_text)
    days_to_expiry = calculate_days_to_expiry(end_date)

    risk_score, priority, recommendation, rationale = score_contract(value, days_to_expiry)

    return ContractAnalysisResult(
        filename=uploaded_file.name,
        value=value,
        start_date=start_date.strftime("%d/%m/%Y") if start_date else "",
        end_date=end_date.strftime("%d/%m/%Y") if end_date else "",
        days_to_expiry=days_to_expiry,
        risk_score=risk_score,
        priority=priority,
        recommendation=recommendation,
        rationale=rationale,
        text_preview=raw_text[:3000],
    )