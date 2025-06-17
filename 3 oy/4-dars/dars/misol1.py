class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Salom, men {self.name}")


class Student(Person):

    def __init__(self, name, surname):
        super().__init__(name)
        self.full_name = self.name + surname
        self.rating = 5
        # super().say_hello()
        # self.say_hello()

    def say_hello(self):
        print(f"Salom, men {self.full_name}")


s = Student("Ali", "Anvarov")
s.say_hello()  # Salom, men Ali
print(s.name)
print(s.rating)
