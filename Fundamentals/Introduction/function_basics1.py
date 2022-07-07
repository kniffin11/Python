print("#1")
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction: 5

print("#2")
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction: error, function undefined 

print("#3")
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction:  5 -- anything after the first return isnt ran

print("#4")
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction: 5 -- anything after the first return isnt ran

print("#5")
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction: 5

print("#6")
def add(b,c):
    print(b+c)
# print(add(1,2) + add(2,3))
# Prediction: 3 5 -- the plus isn't an operator, its a concatenator -- it can but caused error on the above print statement

print("#7")
def concatenate(b,c):
    return str(b)+str(c)
    print(concatenate(2,5))
# Prediction: the funciton isnt called due to indentation, if it were called it would output 25

print("#8")
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction: 100 10 -- b will be printed first 

print("#9")
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction: 7 14 21 -- 3 outputs from 3 function calls

print("#10")
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction: 8

print("#11")
b = 500
print(b)
def foobar():
    # this definition only exists within this function due to scope
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Prediction: 500 500 300 500-- only changes within function call 

print("#12")
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Prediction: 500 500 300 500

print("#13")
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Prediction: 500 500 300 300-- is printed twice since function is assigned to a variable and called as well as printed within the funciton 

print("#14")
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: 1 3 2 

print("#15")
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction: 1 3 5 10 -- 1 comes from foo, 3 and 5 from bar, and 10 from foo 

