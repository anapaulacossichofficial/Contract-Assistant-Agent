from datetime import datetime
from source.parsers import normalize_text, parse_money, parse_dates


def analyze_contract(contract_text: str) -> dict:
    if not contract_text or not contract_text.strip():
        return {
            "summary": "No content extracted from the contract.",
            "risk_score": 0,
            "priority": "Unknown",
            "recommendation": "Upload a valid PDF or DOCX contract.",
            "contract_value": 0.0,
            "start_date": None,
            "end_date": None,
            "days_until_expiration": None,
            "expiration_status": "Unknown",
        }

    normalized = normalize_text(contract_text)
    contract_value = parse_money(contract_text)
    start_date, end_date = parse_dates(normalized)

    today = datetime.today()
    days_until_expiration = None
    expiration_status = "Unknown"
    findings = []

    if end_date:
        days_until_expiration = (end_date.date() - today.date()).days

        if days_until_expiration < 0:
            expiration_status = "Expired"
        elif days_until_expiration <= 30:
            expiration_status = "Critical"
        elif days_until_expiration <= 180:
            expiration_status = "Expiring Soon"
        elif days_until_expiration <= 540:
            expiration_status = "Monitor"
        else:
            expiration_status = "Active"

    # Base principal: vencimento
    if days_until_expiration is None:
        risk_score = 35
        findings.append("Contract end date could not be identified.")
    elif days_until_expiration < 0:
        risk_score = 100
        findings.append("Contract already expired.")
    elif days_until_expiration <= 30:
        risk_score = 90
        findings.append("Contract close to expiration.")
    elif days_until_expiration <= 180:
        risk_score = 65
        findings.append("Contract expiring within 180 days.")
    elif days_until_expiration <= 540:
        risk_score = 45
        findings.append("Contract should be monitored based on expiration timeline.")
    else:
        risk_score = 20
        findings.append("Contract expiration is not imminent.")

    # Peso secundário: valor
    if contract_value >= 1000000:
        risk_score += 12
        findings.append("High contract value identified.")
    elif contract_value >= 500000:
        risk_score += 8
        findings.append("Relevant contract value identified.")
    elif contract_value >= 100000:
        risk_score += 4
        findings.append("Medium contract value identified.")

    # Peso baixo: cláusulas
    clause_score = 0

    if "multa" in normalized:
        clause_score += 2
        findings.append("Penalty clause detected.")

    if "rescis" in normalized:
        clause_score += 2
        findings.append("Termination clause detected.")

    if "reajuste" in normalized:
        clause_score += 2
        findings.append("Price adjustment clause detected.")

    # Limita impacto das cláusulas para não distorcer a demo
    risk_score += min(clause_score, 4)

    # Regra de contenção:
    # se o contrato está muito distante do vencimento (> 540 dias),
    # não pode virar Medium só por cláusulas
    if days_until_expiration is not None and days_until_expiration > 540:
        risk_score = min(risk_score, 39)

    risk_score = min(risk_score, 100)

    if risk_score >= 80:
        priority = "High"
        recommendation = "Review this contract immediately due to the expiration timeline."
    elif risk_score >= 40:
        priority = "Medium"
        recommendation = "Monitor this contract and review the renewal timeline."
    else:
        priority = "Low"
        recommendation = "Proceed with standard review."

    summary = " | ".join(findings)

    return {
        "summary": summary,
        "risk_score": risk_score,
        "priority": priority,
        "recommendation": recommendation,
        "contract_value": contract_value,
        "start_date": start_date.strftime("%d/%m/%Y") if start_date else None,
        "end_date": end_date.strftime("%d/%m/%Y") if end_date else None,
        "days_until_expiration": days_until_expiration,
        "expiration_status": expiration_status,
    }