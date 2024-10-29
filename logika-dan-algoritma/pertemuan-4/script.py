def to_money(amount : float, currency : str) -> str:
    return f"{currency} {amount:,.2f}".replace(",", ".")