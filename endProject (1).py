from typing import Tuple, Callable
import os
import json
import pandas as pd
from Person import Person
from Entry_DB import DB
from student import Student
from Employee import Employee
from Option import Option

def printMenu(menu_option: dict) -> None:
    """dynamicallyprint the menu based on menu_options dictionary"""
    print('\n Main Menu:')
    for num,option in enumerate(menu_option.keys(),start=1):
        print(f'{num}. {option}')
    print(f'{len(menu_option)+1}. Exit')

def printTypesMenu(Option: Option) -> None:
    for num,option in enumerate(Option, start=1):
        print(f'{num}. {option}')
    user_input = userInputIsDigit('Please enter the type of Person you want to save: ')
    if 1 <= user_input <= len(Option):
        return Option(user_input) 


def saveNewStudent(db: DB, person: Person) -> None:
    user_input_subject = input('SUbject of study: ')
    user_input_gpa = userInputIsDigit('GPA: ')
    db.saveNewEntry(Student(person.id, person.name, person.age, user_input_gpa, user_input_subject='NDA'))
    print(f'Entry with id of {person.id} was successfully saved\n')

def saveNewEmployee(db: DB, person: Person) -> None:
    user_input_salary = userInputIsDigit('Salary: ')
    user_input_position = input('Position: ')
    db.saveNewEntry(Employee(person.id, person.name, person.age, user_input_salary, user_input_position='NDA'))
    print(f'Entry with id of {person.id} was successfully saved\n')
    
def userInputIsDigit(input_message: str) -> int:
    user_input = input(input_message)
    while not user_input.isdigit() or '-' in user_input:
        user_input = input(input_message)
    return int(user_input)

def validName(name: str) -> bool:
    signs = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '!', '@', '#', '$', '%', '^', '&', '(', ')', '+', '=', '{', '}', '[', ']', ';', ',', ' ']
    for sign in signs:
        if sign in name:
            return False
    return True


def userInputIsName(input_message: str) -> str:
    user_input = input(input_message)
    valid = validName(user_input)
    while not valid:
        user_input = input(input_message)
        valid =  not validName(user_input)
    return user_input    

def saveNewEntry(db: DB) -> None: #the function for the first option
    user_input_id = userInputIsDigit('ID: ')
    if user_input_id in db.DB_dict:
        print(f'Error: {user_input_id} already exists\n')
        return
    user_input_name = input('Name: ')
    user_input_age = userInputIsDigit('Age: ')
    user_input = printTypesMenu(Option)
    if user_input == Option.Student:
        saveNewStudent(db, Person(user_input_id, user_input_name, user_input_age))  
    elif user_input == Option.Employee:
        saveNewEmployee(db, Person(user_input_id, user_input_name, user_input_age))
    else:
        db.saveNewEntry(Person(user_input_id, user_input_name, user_input_age))  
        print(f'Entry with id of {user_input_id} was successfully saved\n')

def searchByID(db: DB): # the function for the scond option
    user_input = userInputIsDigit('Please enter the ID you want to look for: ')
    db.searchByID(user_input)

def printAgeAverage(db: DB) -> float: # the function for the third option
    db.printAgeAverage()

def printAllNames(db: DB): # the function for the fourth option
    db.printAllNames()

def printAllIDs(db: DB): # the function for the fifth option
    db.printAllIDs()

def printAllEntries(db: DB): # the function for the sixth option
    db.printAllEntries()

def printEntryByIndex(db: DB): # the function for the seventh option
    user_input = userInputIsDigit('Please enter the index of the entry you want to print: ')
    if user_input >= len(db.id_list) or user_input < 0:
        print('Error: input invalid\n')
    else:
        db.printEntryByIndex(user_input)

def saveAllEntries(db: DB) -> None:
    user_input = userInputIsName('what is the name of the file you want to save the entries in(with out .csv)? ')
    db.prepareToSave()
    db.saveDB(user_input+'.csv')
    print('All entries were saved')

def exitProgram() -> bool: # the function for the eighth option
    user_input = input('Are you sure you want to exit? (y/n)').lower()
    global running
    working = True  
    while working:
        if user_input == 'y':
            running = False
            return False
        elif user_input == 'n':
            return True
        else:
            user_input = input('Are you sure you want to exit? (y/n)').lower()

def main():
    db = DB()
    while True:
        menu_option = {
            "Save a new entry": lambda: saveNewEntry(db),
            "Search by ID": lambda: searchByID(db),
            "Print age average": lambda: printAgeAverage(db),
            "Print all names": lambda: printAllNames(db),
            "Print all IDs": lambda: printAllIDs(db),
            "Print all entries": lambda: printAllEntries(db),
            "Print entry by index": lambda: printEntryByIndex(db),
            "Save all entries": lambda: saveAllEntries(db)
        }
        try:
            printMenu(menu_option)
            user_input = userInputIsDigit('Please enter your choice: ')
            if user_input == len(menu_option) + 1:
                if not exitProgram():
                    break
            elif 1 <= user_input <= len(menu_option):
                menu_option[list(menu_option.keys())[user_input - 1]]()
            else:
                print('ERROR: Invalid input, choose a valid option!\n')

        except Exception as e:
            print('oops it sliped out of place im sorry the '+ e + ' had a problem')
            
if __name__ == '__main__':
    running= True
    while running:
        try:
            main()
        except (KeyboardInterrupt, EOFError,Exception) as e:
            print(f'something went wrong but i cought it \n')
            
