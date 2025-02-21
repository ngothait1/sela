from Person import Person

class Student(Person):
    _subject_of_study: str
    _GPA: float
    def __init__(self, id, name, age, GPA, Subject_of_study):
        super().__init__(id, name, age)
        self._subject_of_study = Subject_of_study
        self._GPA = GPA

    def toString(self):
        super().toString()
        print(f'Subject of study: {self._subject_of_study}, GPA: {self._GPA}')

    @property
    def Subject_of_study(self):
        return self._subject_of_study
    
    @Subject_of_study.setter
    def Subject_of_study(self, value):
        self._subject_of_study = value
    
    @property
    def GPA(self):
        return self._GPA
    
    @GPA.setter
    def GPA(self, value):
        self._GPA = value

    
if __name__ == '__main__':
    student = Student(1, 'John', 20, 'Computer Science', 3.5)
    student.toString()
    student.GPA = 4.0
    student.toString()
    student.Subject_of_study = 'Math'
    student.toString()
    student.age = 21
    student.toString()
    student.id = 2
    student.toString()
    id_to_check = 2
    name_to_check = 'Sela'
    age_to_check = 22
    subject_to_check = 'Math'
    gpa_to_check = 3.0
    sela = Student(id_to_check, name_to_check, age_to_check, subject_to_check, gpa_to_check)
    if sela.id != id_to_check:
        print(f"Error: id should be {id_to_check} but it is {sela.id}")
    elif sela.name != name_to_check:
        print(f"Error: name should be {name_to_check} but it is {sela.name}")
    elif sela.age != age_to_check:
        print(f"Error: age should be {age_to_check} but it is {sela.age}")
    elif sela.Subject_of_study != subject_to_check:
        print(f"Error: Subject of study should be {subject_to_check} but it is {sela.Subject_of_study}")
    elif sela.GPA != gpa_to_check:
        print(f"Error: GPA should be {gpa_to_check} but it is {sela.GPA}")
    else:
        print("All tests passed")

    