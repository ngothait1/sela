# save data with the following format:
# [name, age, id]

# the functionality is :
#saving a new person
#search a person by id
#print a age avrage of all records
#print all the names
#print all ids
#print all the records
#print a specific record by index

def printMenu():
    print('1. Save a new entry \n2. Search by ID \n3. Print age average \n4. Print all names \n5. Print all IDs \n6. Print all entries \n7. Print entry by index \n8. Exit')

def userInputIsDigit(input_message: str) -> int:
    user_input = input(input_message)
    while not user_input.isdigit():
        user_input = input(input_message)
    
    return int(user_input)


def printEntry(entry_dict: dict, id: int):
    print(f'ID: {id}, Name: {entry_dict[id][0]}, Age: {entry_dict[id][1]}')

from typing import Tuple

def saveNewEntry(entry_dict: dict,id_list: list,total_age: int, num_of_entries: int) -> Tuple[int, int]: #the function for the first option
    user_input_id = userInputIsDigit('ID: ')
    if user_input_id in entry_dict:
        print(f'Error: {user_input_id} already exists\n')
        return (total_age, num_of_entries)
    user_input_name = input('Name: ')
    user_input_age = userInputIsDigit('Age: ')
    entry_dict[user_input_id] = [user_input_name, user_input_age]
    id_list.append(user_input_id)
    total_age += int(user_input_age)
    print(f'Entry with id of {user_input_id} was successfully saved\n')
    return (total_age, num_of_entries + 1)
    

def searchByID(entry_dict: dict): # the function for the scond option
    user_input = userInputIsDigit('Please enter the ID you want to look for: ')
    if user_input in entry_dict:
        printEntry(entry_dict, user_input)
    else:
        print(f'Error: {user_input} not found\n')
    



def printAgeAverage(total_age: int, num_of_entries: int) -> float: # the function for the third option
    if num_of_entries == 0:
        print('Error: no entries found\n')
    else:
        print(f'{total_age/num_of_entries}')


def printAllNames(entry_dict: dict): # the function for the fourth option
    for id in entry_dict:
        print(entry_dict[id][0])

def printAllIDs(entry_dict: dict): # the function for the fifth option
    for id in entry_dict:
        print(id)

def printAllEntries(entry_dict: dict): # the function for the sixth option
    for id in entry_dict:
        printEntry(entry_dict, id)

def printEntryByIndex(entry_dict: dict, id_list: list): # the function for the seventh option
    user_input = userInputIsDigit('Please enter the index of the entry you want to print: ')
    if user_input < len(id_list):
        printEntry(entry_dict, id_list[user_input])
    else:
        print(f'Error: Index {user_input} not found\n')

def exit(): # the function for the eighth option
    user_input = input('Are you sure you want to exit? (y/n)').lower()
    while True:
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            user_input = input('Are you sure you want to exit? (y/n)').lower()


def main():
    entry_dict = {}
    id_list = []
    total_age = 0
    age_tuple = (0,0)
    num_of_entries = 0
    while True:
        printMenu()
        user_input = input('Please enter youre choice: ')
        if user_input == '1':
            age_tuple = saveNewEntry(entry_dict, id_list, total_age,num_of_entries)
            total_age = age_tuple[0]
            num_of_entries = age_tuple[1]
        elif user_input == '2':
            searchByID(entry_dict)
        elif user_input == '3':
            printAgeAverage(total_age, num_of_entries)
        elif user_input == '4':
            printAllNames(entry_dict)
        elif user_input == '5':
            printAllIDs(entry_dict)
        elif user_input == '6':
            printAllEntries(entry_dict)
        elif user_input == '7':
            printEntryByIndex(entry_dict, id_list)
        elif user_input == '8':
            
            break


main()