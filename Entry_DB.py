import pandas as pd
from Person import Person


class Entry_DB:
    _DB_dict: dict[int, Person] = {}
    _id_list: list[int] = []
    _total_age: int = 0
    _num_of_entries: int = 0
    _DB_to_save: list[dict[int, Person]] = [{}]

    def __init__(self):
        self._DB_dict = {}
        self._id_list = []
        self._total_age = 0
        self._num_of_entries = 0
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
    def num_of_entries(self):
        return self._num_of_entries
    
    @property
    def DB_to_save(self):
        return self._DB_to_save
    
    def saveNewEntry(self, Person: Person )-> None:
        self._DB_dict[Person.id] = Person
        self._id_list.append(Person.id)
        self._total_age += Person.age
        self._num_of_entries += 1

    def searchByID(self, id: int) -> None:
        if id not in self._DB_dict:
            print(f'Error: {id} not found\n')
        else:
            print(f' ID: {id} Name: {self._DB_dict[id].name} Age: {self._DB_dict[id].age}')

    def printAgeAverage(self) -> None:
        if self._num_of_entries == 0:
            print('Error: no entries found\n')
        else:
            print(f'{self._total_age / self._num_of_entries}')
    
    def printAllNames(self) -> None:
        for id in self._DB_dict:
            print(self._DB_dict[id].name)
    
    def printAllIDs(self) -> None:
        for id in self._DB_dict:
            print(id)
    
    def printAllEntries(self) -> None:
        for id in self._DB_dict:
            print(f'ID: {id}, Name: {self._DB_dict[id].name}, Age: {self._DB_dict[id].age}')
    
    def printEntryByIndex(self, index: int) -> None:
        if index >= self._num_of_entries:
            print(f'Error:(out of range) {index} not found\n')
        elif index < 0:
            print(f'Error: (minus index) {index} not found\n')
        elif self._num_of_entries == 0:
            print('Error: no entries found\n')
        else:
            print(f'ID: {self._id_list[index]}, Name: {self._DB_dict[self._id_list[index]].name}, Age: {self._DB_dict[self._id_list[index]].age}')
        
    def prepareToSave(self,headers: list[str]) -> None:
        for id in self._DB_dict:
            self._DB_to_save.append({headers[0]: id, headers[1]: self._DB_dict[id].name, headers[2]: self._DB_dict[id].age})

    def saveDB(self,FileNameToSave: str) -> None:
        file_path = f'C:/Users/USER/Desktop/program/python/third/endProject/{FileNameToSave}' 
        pd.DataFrame(self._DB_to_save).to_csv(file_path, index=False)
