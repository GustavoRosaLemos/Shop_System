class Card:
    def __init__(self, number, ccv, date, funds):
        self.number = number
        self.ccv = ccv
        self.date = date
        self.funds = funds

    def getnumber(self):
        return self.number

    def getccv(self):
        return self.ccv

    def getdate(self):
        return self.date

    def getfunds(self):
        return self.funds
