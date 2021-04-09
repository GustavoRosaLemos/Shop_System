class Card:
    def __init__(self, number, ccv, funds):
        self.number = number
        self.ccv = ccv
        self.funds = funds

    def get_number(self):
        return self.number

    def get_ccv(self):
        return self.ccv

    def get_funds(self):
        return self.funds
