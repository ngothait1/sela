class Util:
    def __init__(self):
        pass

    @staticmethod
    def userInputIsDigit(input_message: str) -> int:
        user_input = input(input_message)
        while not user_input.isdigit() or '-' in user_input:
            print("Invalid input. Please enter a digit.")
            user_input = input(input_message)
        return int(user_input)
        
    @staticmethod
    def validString(name: str) -> bool:
        signs = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '!', '@', '#', '$', '%', '^', '&', '(', ')', '+', '=', '{', '}', '[', ']', ';', ',', ' ']
        for sign in signs:
            if sign in name:
                return False
        return True
    
    @staticmethod
    def userInputIsString(input_message: str) -> str:
        user_input = input(input_message)
        valid = Util.validString(user_input)
        while not valid:
            print("Invalid input. Please enter a valid name.")
            user_input = input(input_message)
            valid = Util.validString(user_input)
        return user_input


