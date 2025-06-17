class Developer:
    def __init__(self,sername,position,salary):
        self.sername = sername
        self.position = position
        self.salary = salary
class SoftwareEngineer(Developer):
    def __init__(self,bonus,department):
        self.bonus = bonus
        self.department = department

