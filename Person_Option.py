from enum import Enum
from Person import Person
from Student import Student
from Employee import Employee
from Util import Util

class Person_Option(Enum):
    Person = 1
    Student = 2
    Employee = 3
    
    def create_instance(self, id: int, name: str, age: int):
        if self == Person_Option.Person:
            return Person(id, name, age)
        elif self == Person_Option.Student:
            user_input_subject = Util.userInputIsString('Please enter the subject of study of the new entry: ')
            user_input_gpa = Util.userInputIsDigit('Please enter the GPA of the new entry: ')
            return Student(id, name, age, user_input_subject, user_input_gpa)
        elif self == Person_Option.Employee:
            user_input_salary = Util.userInputIsDigit('Please enter the salary of the new entry: ')
            user_input_position = Util.userInputIsString('Please enter the position of the new entry: ')
            return Employee(id, name, age, user_input_salary, user_input_position)
        return None
      

