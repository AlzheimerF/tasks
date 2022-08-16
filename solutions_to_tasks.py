"""@
# TODO task #1:
def strannosti():
    a = int(input("Введите целое число: "))
    if a % 2 != 0:
        print("Weird")
    elif a % 2 == 0 and 2 <= a <= 5:
        print("Not Weird")
    elif a % 2 == 0 and 6 <= a <= 20:
        print("Weird")
    elif a % 2 == 0 and a > 20:
        print("Not Weird")

# strannosti()

"""

"""
# TODO task #2:
def calc_year():
    year = int(input("Введите год: "))
    if year % 4 != 0:
        print("Год обычный")
    elif year % 100 != 0:
        print("Год високосный")
    elif year % 400 == 0:
        print("Год високосный")
    else:
        print("Год обычный")

# calc_year()

"""

"""
# TODO task #3:
class Taking_credit:
    def __init__(self, n, y, p):
        self.n = n
        self.y = y
        self.p = p / 100
        self.m = int((self.n * self.p * (1 + self.p) * self.y) / (12 * ((1 + self.p) * self.y - 1)))
        self.s = (self.m * 12) * self.y
    def in_month(self):
        return f"Ваш месячный платеж составит: {self.m} сом "

    def to_all_month(self):
        return f"За весь период вы заплатите: {self.s} сом"

class Giving_credit:
    def in_month(self, *args):
        self.itog = 0
        for credit in args:
            self.m = int((credit.n * credit.p * (1 + credit.p) * credit.y) / (12 * ((1 + credit.p) * credit.y - 1)))
            self.itog += self.m
        return f"Со всех людей, берущих у вас кредит, Ваша выручка в месяц: {self.itog} сом. "




credit1 = Taking_credit(100_000_0, 10, 15)
credit2 = Taking_credit(100_000_00, 10, 15)
credit3 = Taking_credit(100_000_000, 10, 15)

c = Giving_credit()
print(c.in_month(credit1, credit2, credit3))

"""
