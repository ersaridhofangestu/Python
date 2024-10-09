class Format:
    def ToMoney(self, amount, currency):
        return f"{currency} {amount:,.0f}".replace(",", ".")
