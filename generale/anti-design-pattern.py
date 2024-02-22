from abc import ABC, abstractmethod

"""
Versione standard utilizzando il riferimento super alla classe parent
"""


class Report1:

    def make_report(self):
        "HEADER dei report da generare nelle classi figlie"
        print("Company " + self.company)


class SalesReport1(Report1):
    "classe report delle vendite"

    def __init__(self, company, sales) -> None:
        self.company = company
        self.sales = sales

    def make_report(self):
        "HEADER preso dalla classe padre, corpo nel metodo"

        super().make_report()
        print("Sales " + str(self.sales))


class CostReport1(Report1):
    "classe report dei costi"

    def __init__(self, company, costs) -> None:
        self.company = company
        self.costs = costs

    def make_report(self):
        "HEADER preso dalla classe padre, corpo nel metodo"

        super().make_report()
        print("Costs " + str(self.costs))


a = SalesReport1("Amazon", 10000)
b = CostReport1("Google", 100)

# a.make_report()
# print("-" * 40)
# b.make_report()


print("%" * 50)

"""
Template Method Design Pattern ----------------------------------------
"""


class Report(ABC):

    @abstractmethod
    def make_report_body(self):
        "metodo astratto che forza la chiamata ai metodi figli"

    def make_report(self):
        "HEADER dei report da generare nelle classi figlie"

        print("Company " + self.company)
        self.make_report_body()  # riferimento ai metodi figli


class SalesReport(Report):
    "classe report delle vendite"

    def __init__(self, company, sales) -> None:
        self.company = company
        self.sales = sales

    def make_report_body(self):
        "HEADER preso dalla classe padre, corpo locale"

        print("Sales " + str(self.sales))


class CostReport(Report):
    "classe report dei costi"

    def __init__(self, company, costs) -> None:
        self.company = company
        self.costs = costs

    def make_report_body(self):
        "HEADER preso dalla classe padrea, corpo in locale"
        print("Costs " + str(self.costs))


# creo istanza report vendite, report costi
a = SalesReport("Amazon", 10000)
b = CostReport("Google", 100)

# richiamo metodo nella classe padre
a.make_report()
print("-" * 40)
b.make_report()
