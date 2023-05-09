class Vacancy:

    def __init__(self, name, url, payment, requrements):
        self.name = name
        self.url = url
        self.payment = payment
        self.requrements = requrements  

    def __str__(self):
        return f"{self.name}, {self.url}, {self.payment}, {self.requrements};"

    def __lt__(self, objeckt_2):
        return self.payment < objeckt_2.payment

    def __le__(self, objeckt_2):
        return self.payment <= objeckt_2.payment

    def __gt__(self, objeckt_2):
        return self.payment > objeckt_2.payment

    def __ge__(self, objeckt_2):
        return self.payment >= objeckt_2.payment

    def __eq__(self, objeckt_2):
        return self.payment == objeckt_2.payment