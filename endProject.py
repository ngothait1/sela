from typing import Tuple
import os
import json
import pandas as pd
from Person import Person
from Entry_DB import Entry_DB
from student import Student


def printMenu():
    print('1. Save a new entry')
    print('2. Search by ID') 
    print('3. Print age average')
    print('4. Print all names')
    print('5. Print all IDs')
    print('6. Print all entries')
    print('7. Print entry by index')
    print('8. Save all entries')
    print('9. Exit')

def userInputIsDigit(input_message: str) -> int:
    user_input = input(input_message)
    while not user_input.isdigit() or '-' in user_input:
        user_input = input(input_message)
    return int(user_input)


def validFileName(file_name: str) -> bool:
    signs = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '!', '@', '#', '$', '%', '^', '&', '(', ')', '+', '=', '{', '}', '[', ']', ';', ',', ' ']
    for sign in signs:
        if sign in file_name:
            return False
    return True

def userInputIsFileName(input_message: str) -> str:
    user_input = input(input_message)
    valid = validFileName(user_input)
    while not valid:
        user_input = input(input_message)
        valid =  not validFileName(user_input)
    return user_input    


# def printEntry(entry_dict: dict, id: int):
#     print(f'ID: {id}, Name: {entry_dict[id][0]}, Age: {entry_dict[id][1]}')

def saveNewEntry(DB: Entry_DB) -> None: #the function for the first option
    user_input_id = userInputIsDigit('ID: ')
    if user_input_id in DB.DB_dict:
        print(f'Error: {user_input_id} already exists\n')
    user_input_name = input('Name: ')
    user_input_age = userInputIsDigit('Age: ')
    DB.saveNewEntry(Person(user_input_id, user_input_name, user_input_age))  
    print(f'Entry with id of {user_input_id} was successfully saved\n')#############################################################################################################

def searchByID(DB: Entry_DB): # the function for the scond option
    user_input = userInputIsDigit('Please enter the ID you want to look for: ')
    DB.searchByID(user_input)

def printAgeAverage(DB: Entry_DB) -> float: # the function for the third option
    DB.printAgeAverage()

def printAllNames(DB: Entry_DB): # the function for the fourth option
    DB.printAllNames()

def printAllIDs(DB: Entry_DB): # the function for the fifth option
    DB.printAllIDs()

def printAllEntries(DB: Entry_DB): # the function for the sixth option
    DB.printAllEntries()

def printEntryByIndex(DB: Entry_DB): # the function for the seventh option
    user_input = userInputIsDigit('Please enter the index of the entry you want to print: ')
    DB.printEntryByIndex(user_input)

def retrieveConf() -> list[str]:
    with open(r'C:\Users\USER\Desktop\program\python\third\ENDPROJECT\conf.json', 'r') as json_file:
        conf = json.load(json_file)
        headers= [conf['id'], conf['name'], conf['age']]
    return headers

# def formatedEntryStorage(entry_dict: dict, headers: list[str]) -> list[dict]:
#     to_save_dict = []
#     for id in entry_dict:
#         to_save_dict.append({headers[0]: id, headers[1]: entry_dict[id][0], headers[2]: entry_dict[id][1]})
#     return to_save_dict

# def saveAllEntries(entry_dict: dict): # the function for the eighth option
#     user_input = userInputIsFileName('what is the name of the file you want to save the entries in(with out .csv)? ')
#     headers = retrieveConf()
#     to_save_dict = formatedEntryStorage(entry_dict, headers)
#     df = pd.DataFrame(to_save_dict)
#     path_of_file = os.path.join(r'C:\Users\USER\Desktop\program\python\third\midProject', user_input+'.csv')
#     df.to_csv(path_of_file, index=False)
#     print('All entries were saved') 

def prepareToSave(DB: Entry_DB) -> None:
    headers = retrieveConf()
    DB.prepareToSave(headers)

def saveAllEntries(DB: Entry_DB) -> None:
    user_input = userInputIsFileName('what is the name of the file you want to save the entries in(with out .csv)? ')
    prepareToSave(DB)
    DB.saveDB(user_input+'.csv')
    print('All entries were saved')

def exitProgram() -> bool: # the function for the eighth option
    user_input = input('Are you sure you want to exit? (y/n)').lower()
    working = True  
    while working:
        if user_input == 'y':
            return False
        elif user_input == 'n':
            return True
        else:
            user_input = input('Are you sure you want to exit? (y/n)').lower()


def main():
    DB = Entry_DB()
    while True:
        printMenu()
        user_input = input('Please enter youre choice: ')
        if user_input == '1':
            saveNewEntry(DB)
        elif user_input == '2':
            searchByID(DB)
        elif user_input == '3':
            printAgeAverage(DB)
        elif user_input == '4':
            printAllNames(DB)
        elif user_input == '5':
            printAllIDs(DB)
        elif user_input == '6':
            printAllEntries(DB)
        elif user_input == '7':
            printEntryByIndex(DB)
        elif user_input == '8':
            saveAllEntries(DB)
        elif user_input == '9':
            global running 
            running = exitProgram()
            break


running= True
while running:
    try:
        main()
    except (Exception,KeyboardInterrupt) as e:
        print(f'Error: the last process failed.\n reason : {e}')
    finally:
        print('thanks you have a good day')
