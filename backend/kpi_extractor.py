import re

def extract_kpis(text):
    kpis = {}

    revenue_match = re.search(r"revenue(?:\s+\w+)*?\s*[\$₹€]?\s*([\d,\.]+)", text, re.IGNORECASE)
    if revenue_match:
        kpis['revenue'] = revenue_match.group(1)

    profit_match = re.search(r"(net\s+profit|profit\s+after\s+tax|net\s+income)(?:\s+\w+)*?\s*[\$₹€]?\s*([\d,\.]+)", text, re.IGNORECASE)
    if profit_match:
        kpis['profit'] = profit_match.group(2)

    margin_match = re.search(r"(profit\s+margin|net\s+margin)(?:\s+\w+)*?\s*([\d\.]+%)", text, re.IGNORECASE)
    if margin_match:
        kpis['margin'] = margin_match.group(2)

    # Add more KPIs if needed

    return kpis
