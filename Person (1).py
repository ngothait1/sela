class Person:
    _id: int
    _name: str
    _age: int
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age


    def toString(self):
        print(f'ID: {self._id}, Name: {self._name}, Age: {self._age}')

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value