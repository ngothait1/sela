from Person import Person

class Employee(Person):
    _Salary: float
    _Position: str
    
    def __init__(self, id, name, age, Salary, Position):
        super().__init__(id, name, age)
        self._Salary = Salary
        self._Position = Position

    def toString(self):
        super().toString()
        print(f'Salary: {self._Salary}, Position: {self._Position}')

    @property
    def Salary(self):
        return self._Salary
    
    @Salary.setter
    def Salary(self, value):
        self._Salary = value
    
    @property
    def Position(self):
        return self._Position
    
    @Position.setter
    def Position(self, value):
        self._Position = value