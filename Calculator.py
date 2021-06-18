# Michael McAdow
# 7/5/20
# Calculator.py
# Program that allows user to select one of four different arithmetic
# operations and then compute two numbers accordingly.

operator = ''
first_num = 0
second_num =  0
total = 0

operator = input('Please select one option: add/subtract/multiply/divide: ')
first_num = input('What is the first number? ')
second_num = input('What is the second number? ')

first_num = float(first_num)
second_num = float(second_num)


if operator == 'add':
    print('You chose ' + (operator) + '.')
    total = (first_num+second_num)
    operator = '+'
elif operator == 'subtract':
    print('You chose ' + (operator) + '.')
    total = (first_num-second_num)
    operator = '-'
elif operator == 'multiply':
    print('You chose ' + (operator) + '.')
    total = (first_num*second_num)
    operator = '*'
elif operator == 'divide':
    print('You chose ' + (operator) + '.')
    total = (first_num/second_num)
    operator = '/'
else: 
    print('The option you chose, "' + (operator) + '" is not valid.')
    print('Please try this program again with a correct option.')
    exit()


first_num = round(first_num,2)
second_num = round(second_num,2)

print (str(first_num ) + " " 
      + str(operator) + " " 
      + str(second_num) + " = " 
      + str(round(total,2)))
print ('\nThank you for using my calculator, have a nice day!\n')