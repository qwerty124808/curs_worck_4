class Vacancy:

    def __init__(self, sourse, id, name, client, url, area, payment_min, payment_max, currency):
        self.sourse = sourse
        self.id = id
        self.name = name
        self.client = client
        self.url = url
        self.area = area
        self.salary_correkt(payment_min, payment_max)
        self.currency = currency
        

    def corect_vaccansy(self):
        return {
            "sourse": self.sourse,
            "id": self.id,
            "name": self.name,
            "client": self.client,
            "url":  self.url,
            "area": self.area,
            "payment_min": self.payment_min,
            "payment_max": self.payment_max,
            "currency": self.currency,
        } 

    def salary_correkt(self, min, max):
        if max is None:
            self.payment_max = 0
            self.payment_min = min
        elif min is None:
            self.payment_min = 0
            self.payment_max = max
        else:
            self.payment_max = max
            self.payment_min = min



    def __str__(self):
        return f"{self.name}, {self.url}, {self.payment_min}, {self.payment_max}, {self.currency};"

    def __lt__(self, objeckt_2):
        return self.payment_max < objeckt_2.payment_max

    def __le__(self, objeckt_2):
        return self.payment_max <= objeckt_2.payment_max

    def __gt__(self, objeckt_2):
        return self.payment_max > objeckt_2.payment_max

    def __ge__(self, objeckt_2):
        return self.payment_max >= objeckt_2.payment_max

    def __eq__(self, objeckt_2):
        return self.payment_max == objeckt_2.payment_max