class Person:
    def __init__(self, name, adress):
        self.__name = name
        self.__adress = adress

    @property
    def name(self):
        return self.__name

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, new_adress):
        self.__adress = new_adress

    def __str__(self):
        return self.name, self.adress



class Student(Person):
    def __init__(self,name, adress,courses:list=[],grades:list=[]):
        super().__init__(name, adress)
        self.courses = courses
        self.grades = grades

    def add_course_grade(self, course: str, grade: int):
        self.courses.append(course)
        self.grades.append(grade)

    def print_grades(self):
        for course, grade in zip(self.courses,self.grades):
            print(course, grade)
        # for i in range(len(self.grades)):
        #     print(self.courses[i], self.grades[i])

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student:{self.name}{self.adress}"
class Teacher(Person):
    def __init__(self,name,courses:list=[str],grades:list=[]):
        super().__init__(name,courses)
        self.grades = grades
        




s1 = Student("Ali", "Tashkent")
s1.add_course_grade("Math", 90)
s1.add_course_grade("English", 80)
s1.print_grades()
print(s1.to_string())  # Student: Ali(Tashkent)
s1.print_grades()
print("O'rtacha baho:", s1.get_average_grade())

t1 = Teacher("Gulbahor", "Samarqand")
t1.add_course("Math")
t1.add_course("Physics")
t1.remove_course("Math")

print(t1.to_string())  # Teacher: Gulbahor(Samarqand)