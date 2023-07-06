# class Student:
#     name="Maureen"
#     age=23
#     student="AkiraChix"
#     country="Kenya"

class Student:
    school="Akirachix"
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country

    def greet_student(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}"    