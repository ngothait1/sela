import time

print('Hello, This is my final project')
name = input('what is your name? ')
print(f'Hi {name}, nice to meet you \n This is a special caculator, i would need two numbers from you')
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
print (f'thanks you for putting in youre numbers, {number1} and {number2}' )
total = 0
date = time.ctime()
operator = ''
valid = True
num1_state = ''
num2_state = ''
if number1 % 2 == 0:
 num1_state='even'
else:
 num1_state='odd' 
if number2 % 2 == 0:
 num2_state='even'
else:
 num2_state='odd'

if num1_state == num2_state:
    print(f'Both numbers are {num1_state}')
else:
    print(f'Number 1 is {num1_state} and Number 2 is {num2_state}')


operator=input('Enter the operator you want to use( + , - , * , / ): ')
if operator == '+':
    total=number1 + number2
elif operator == '-':
        total=number1 - number2
elif operator == '*':
        total=number1 * number2
elif operator == '/':
        question=input('you chose to divide would you like the result to be integer ? (yes/no): ')
        if number2 == 0:
            print('You cannot divide by zero')
            valid=False
        elif question == 'yes':
            total=number1 // number2
        elif question == 'no':
            total=number1 / number2
        else:
                print('Invalid input')
                valid=False 
            


        
            
else:
    print('Invalid operator')
    valid=False

if valid:
 print(f'{number1} {operator} {number2} = {total}')
else:
    print('something went wrong, please try again')

print(f'Thank you {name} for using this calculator on {date}')
