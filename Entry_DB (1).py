import pandas as pd
from Person import Person
from student import Student
from Employee import Employee   
from Option import Option

class DB:
    _DB_dict: dict[int, Person] = {}
    _id_list: list[int] = []
    _total_age: int = 0
    _DB_to_save: list[dict[int, Person]] = [{}]

    def __init__(self):
        self._DB_dict = {}
        self._id_list = []
        self._total_age = 0
        self._DB_to_save = [{}]

    @property
    def DB_dict(self):
        return self._DB_dict
    
    @property
    def id_list(self):
        return self._id_list
    
    @property
    def total_age(self):
        return self._total_age
    
    @property
    def DB_to_save(self):
        return self._DB_to_save
    
    def saveNewEntry(self, person: Person )-> None:
        if person.id in self._DB_dict:
            print(f'Error: {person.id} already exists\n')
        self._DB_dict[person.id] = person
        self._id_list.append(person.id)
        self._total_age += person.age

    def searchByID(self, id: int) -> None:
        if id not in self._DB_dict:
            print(f'Error: {id} not found\n')
        else:
           self._DB_dict[id].toString()

    def printAgeAverage(self) -> None:
        if len(self._DB_dict) == 0:
            print('Error: no entries found\n')
        else:
            print(f'{self._total_age / len(self._DB_dict)}')
    
    def printAllNames(self) -> None:
        for id in self._DB_dict:
            print(self._DB_dict[id].name)
    
    def printAllIDs(self) -> None:
        for id in self._DB_dict:
            print(id)
    
    def printAllEntries(self) -> None:
        for id in self._DB_dict:
            self._DB_dict[id].toString()
    
    def printEntryByIndex(self, index: int) -> None:
        self._DB_dict[self._id_list[index]].toString()

    def prepareToSave(self) -> None:
        for id in self._DB_dict:
            self._DB_to_save.append({'ID': id, 'Name': self._DB_dict[id].name, 'Age': self._DB_dict[id].age, 'Type': str(type(self._DB_dict[id])), 'subject of study': self._DB_dict[id].Subject_of_study if isinstance(self._DB_dict[id], Student) else 'N/A', 'GPA': self._DB_dict[id].GPA if isinstance(self._DB_dict[id], Student) else 'N/A' , 'position': self._DB_dict[id].Position if isinstance(self._DB_dict[id], Employee) else 'N/A', 'salary': self._DB_dict[id].Salary if isinstance(self._DB_dict[id], Employee) else 'N/A'})

    def saveDB(self,file_name_to_save: str) -> None:
        file_path = f'C:/Users/USER/Desktop/program/python/third/endProject/{file_name_to_save}' 
        pd.DataFrame(self._DB_to_save).to_csv(file_path, index=False)
        print(f'DB was saved in {file_path}\n')