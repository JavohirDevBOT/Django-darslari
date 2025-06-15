from django.utils.dateformat import re_escaped


class Employee:


    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary


class EnterpriseEmployee(Employee):

    def __init__(self, surname, position, salary, rating:int=0):
        super().__init__(surname, position, salary)
        self.rating = rating

    def oshirilgan_oylik(self) -> float:
        if 60 <= self.rating < 75:
            return self.salary + self.salary * 0.2
        elif 75 <= self.rating < 90:
            return self.salary + self.salary * 0.4
        elif 90 <= self.rating <= 100:
            return self.salary + self.salary * 0.6
        return self.rating

    def __str__(self):
        return f"{self.surname} {self.position} {self.salary} {self.oshirilgan_oylik()}"

hodimlar = []

for i in range(2):
    surname = input("Familiya:")
    position = input("Lavozimi:")
    salary = float(input("Maoshi:"))
    rating = float(input("Reyting:"))
    hodim = EnterpriseEmployee(surname, position, salary, rating)
    hodimlar.append(hodim)


for hodim in hodimlar:
    print(hodim)
