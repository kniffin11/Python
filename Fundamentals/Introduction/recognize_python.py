# variable initialization, int
num1 = 42 

# variable initialization, float or decimal
num2 = 2.3

# variable initialization, boolean, true false
boolean = True

# variable initialization, string 
string = 'Hello World'

# list (works like an array) initialization, pizza toppings with 5 string indexes [0-4]
# lists are in square brackets 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# dictionary (works like an array) initialization, variable declaration, ie the key name has the value John
# dictionaries have key value pairs: keys and their values
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# -------------------------------------------------------------------------
#  This is from functions intermediate and helps with asigning wihtin dictionaryoes and lists

# this is a dictionary with a list inside
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'



students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# --------------------------------------------------------------------------

# tuple (works like an array) initialization, 3 values, index [0-2] 
# tuples are in parenthases and are immutable; there is no data assignment
fruit = ('blueberry', 'strawberry', 'banana')

# prints out the type that fruit is: a tuple - can tell by ()'s
print(type(fruit))

# prints out the value at index [1] of pizza_toppings: Sausage
print(pizza_toppings[1])

# this adds Mushrooms to the list of pizza_toppings
pizza_toppings.append('Mushrooms')

# this will print the value of the key name in the dictionary person: John
print(person['name'])

# this assigns the the value of key name to George
person['name'] = 'George'

# this assigns the value of key eye_color to blue
person['eye_color'] = 'blue'

# this returns the index of 2 of the tuple fruit 
print(fruit[2])

# this is a conditional if
if num1 > 45:
    print("It's greater") # if num1 is greater than 45 print Its greater 
else:
    print("It's lower") # if num1 is lower than 45 print Its lower 

# conditional if 
if len(string) < 5:
    print("It's a short word!") # if the string length is less than 5 print its a short world
elif len(string) > 15:
    print("It's a long word!") # if the string length is more than 15 print its a long world
else:
    print("Just right!") # if the string length is bewteen 5 and 15 print just right

# for loop the length of 5, index [0-4]
for x in range(5):
    print(x) # print all of the values

# for loop the length of 5 starting from 2, index [2-4]
for x in range(2,5):
    print(x) # print all of the values

# for loop the length of 10 starting at 2, increasing by 3 each itteration, index [2-9]
for x in range(2,10,3):
    print(x) # print all of the values

# while loop goes until x = 5
x = 0
while(x < 5):
    print(x) # prints value 
    x += 1 # adds one to x every ittertaion 

# removes the last index of the list pizza toppings
pizza_toppings.pop()

# removes the value at the index of 1 from pizza toppings
pizza_toppings.pop(1)

# print the dictionary person in sets of pairs on each line
print(person)

# removes the key and its corresponding value of eye_color
person.pop('eye_color')

# prints the person dicionary without 
print(person)

# for loop that assumes topping is a variable that refers to the index of the list pizza_toppings
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue # if the topping is pepperoni continue to the next print and if statement
    print('After 1st if statement')
    if topping == 'Olives': # if the value at the index is olives then stop the program. It should run until it hits olives
        break

# function with no parameters 
def print_hello_ten_times():
    # for loop that goes from 0-9 
    for num in range(10):
        # prints hello 
        print('Hello')

# funcation call 
print_hello_ten_times()

# function with parameter x 
def print_hello_x_times(x):
    # for loop that goes from 0 to x-1
    for num in range(x):
        # prints hello 
        print('Hello')

# function call with parameter of 4, prints Hello 4 times
print_hello_x_times(4)

# function with parameter of 10 unless otherwise specified
def print_hello_x_or_ten_times(x = 10):
    # for loop that goes from 0 to x-1 or 9 (default is 10)
    for num in range(x):
        # print Hello 
        print('Hello')

# function call without parameter that prints hello 10 times
print_hello_x_or_ten_times()

# function call without parameter that prints hello 4 times
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# print(num3) -- this returns a name error
# num3 = 72 -- this intiializes the variable num3 
# fruit[0] = 'cranberry' -- this gives a type error since you cant change a tuples value
# print(person['favorite_team']) -- key error as it isnt a key in the dictionary person
# print(pizza_toppings[7]) -- this gives an index error as there arent that many indicies in the list pizza_toppings
# print(boolean) -- this returns a name error since boolean isnt defined (even though its a type)
# fruit.append('raspberry') -- this gives a type error since you cant change a tuples value
# fruit.pop(1) -- this gives a type error since you cant change a tuples value

'''
- variable declaration
- log statement
- type check
- length check
- comment
    - single line
    - multiline
- Data Types
    - Primitive
        - Boolean
        - Numbers
        - Strings
    - Composite
        - List 
            - initialize
            - access value
            - change value
            - add value
            - delete value
        - Tuples
            - initialize
            - access value
            - change value
            - add value
            - delete value
        - Dictionary
            - initialize
            - access value
            - change value
            - add value
            - delete value
- conditional
    - if
    - else if
    - else
- for loop
    - start
    - stop
    - increment
    - break
    - continue
    - sequence
- while loop
    - start
    - stop
    - increment
- function
    - parameter
    - argument
    - return

* Bonus: Errors

- NameError: name <variable name> is not defined
- TypeError: 'tuple' object does not support item assignment
- KeyError: 'favorite_team'
- IndexError: list index out of range
- IndentationError: unexpected indent
- AttributeError: 'tuple' object has no attribute 'pop'
- AttributeError: 'tuple' object has no attribute 'append'
- Tuples
    - change value
    - add value
    - delete value
'''