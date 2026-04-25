from datetime import datetime
from source.parsers import parse_money, parse_dates
from source.scoring import score_contract

def test_parse_money_contract_a():
    text = "VALOR ESTIMADO R$ 5.400.000,00 por ano."
    assert parse_money(text.lower()) == 5400000.00

def test_parse_money_contract_b():
    text = "VALOR ESTIMADO R$ 820.000,00 por ano."
    assert parse_money(text.lower()) == 820000.00

def test_parse_money_contract_c():
    text = "VALOR ESTIMADO R$ 240.000,00 por ano."
    assert parse_money(text.lower()) == 240000.00

def test_parse_dates_contract_a():
    text = "PRAZO DE VIGENCIA 12 meses, com inicio em 01/05/2025 e termino em 30/04/2026"
    start, end = parse_dates(text.lower())
    assert start == datetime(2025, 5, 1)
    assert end == datetime(2026, 4, 30)

def test_parse_dates_contract_b():
    text = "PRAZO DE VIGENCIA 24 meses, com inicio em 01/07/2025 e termino em 30/06/2027"
    start, end = parse_dates(text.lower())
    assert start == datetime(2025, 7, 1)
    assert end == datetime(2027, 6, 30)

def test_parse_dates_contract_c():
    text = "PRAZO DE VIGENCIA 36 meses, com inicio em 01/09/2025 e termino em 31/08/2028"
    start, end = parse_dates(text.lower())
    assert start == datetime(2025, 9, 1)
    assert end == datetime(2028, 8, 31)

def test_score_contract_a_high():
    score, priority, recommendation, rationale = score_contract(5_400_000, 7)
    assert priority == "High"
    assert recommendation == "Prioritize renegotiation"
    assert score >= 65
    assert "High-value contract." in rationale
    assert "Near-term expiry." in rationale

def test_score_contract_b_medium():
    score, priority, recommendation, _ = score_contract(820_000, 430)
    assert priority == "Medium"
    assert recommendation == "Monitor and prepare renegotiation"

def test_score_contract_c_low():
    score, priority, recommendation, _ = score_contract(240_000, 850)
    assert priority == "Low"
    assert recommendation == "Low priority"