class Card:
    def __init__(self, number, cvv, date, funds):
        self.number = number
        self.cvv = cvv
        self.date = date
        self.funds = funds

    def getnumber(self):
        return self.number

    def getcvv(self):
        return self.cvv

    def getdate(self):
        return self.date

    def getfunds(self):
        return self.funds
