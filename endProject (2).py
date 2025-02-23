from DB import DB
from Person_Option import Person_Option
from Util import Util

def printMenu(menu_option: dict) -> None:  ## the function to print the main menu
    """dynamicallyprint the menu based on menu_options dictionary"""
    print('\n Main Menu:')
    for num,option in enumerate(menu_option.keys(),start=1):
        print(f'{num}. {option}')
    print(f'{len(menu_option)+1}. Exit')


def printPersonsMenu(Option: Person_Option) -> None: ## the function to print the types of person menu
    for num,option in enumerate(Option, start=1):
        print(f'{num}. {option.name}')
    user_input = Util.userInputIsDigit('Please enter the type of Person you want to save: ')
    if 1 <= user_input <= len(Option):
        return Option(user_input) 
    else:
        print('ERROR: Invalid input, choose a valid option!\n')
        return printPersonsMenu(Option)

def saveNewEntry(db: DB) -> None: #the function for the first option - save a new entry
    user_input = printPersonsMenu(Person_Option)
    user_input_id = Util.userInputIsDigit('Please enter the ID: ')
    if user_input_id in db.id_list:
        print('Error: ID already exists\n')
        saveNewEntry(db)
    else:
        user_input_name = Util.userInputIsString('Please enter the name: ')
        user_input_age = Util.userInputIsDigit('Please enter the age: ')
        new_person = user_input.create_instance(user_input_id, user_input_name, user_input_age)
        db.saveNewEntry(new_person)
        print(f'Entry with id of {new_person.id} was successfully saved\n')
        # new_person = Person_Option[user_input].contstructor(user_input_id, user_input_name, user_input_age)
        # db.saveNewEntry(new_person)
        # print(f'Entry with id of {new_person.id} was successfully saved\n')

def searchByID(db: DB): # the function for the scond option
    user_input = Util.userInputIsDigit('Please enter the ID you want to look for: ')
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
    user_input = Util.userInputIsDigit('Please enter the index of the entry you want to print: ')
    if user_input >= len(db.id_list) or user_input < 0:
        print('Error: input invalid\n')
    else:
        db.printEntryByIndex(user_input)

def saveAllEntries(db: DB) -> None:
    user_input = Util.userInputIsString('what is the name of the file you want to save the entries in(with out .csv)? ')
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
            user_input = Util.userInputIsDigit('Please enter your choice: ')
            if user_input == len(menu_option) + 1:
                if not exitProgram():
                    break
            elif 1 <= user_input <= len(menu_option):
                menu_option[list(menu_option.keys())[user_input - 1]]()
            else:
                print('ERROR: Invalid input, choose a valid option!\n')

        except Exception as e:
            print(e)
            
if __name__ == '__main__':
    running= True
    while running:
        try:
            main()
        except (KeyboardInterrupt, EOFError,Exception) as e:
            print(e)
       
            
