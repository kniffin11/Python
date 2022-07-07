# --------------------------------- Problem 1 ----------------------------------------

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x [1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# print(sports_directory, end = " ")

# Change the value 20 in z to 30
z[0]['y'] = 30

print(sports_directory)
print(students)
print(z)

# --------------------------------- Problem 2 ----------------------------------------

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range (0, len(students)):
        print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# --------------------------------- Problem 3 ----------------------------------------

def iterateDictionary2(key, list):
    for i in range (0, len(list)):
        print(students[i][key])

iterateDictionary2('first_name', students)

# --------------------------------- Problem 4 ----------------------------------------

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(x):
    # creates a list of the keys wihtin given dictionary
    arr = list(x.keys())

    #  this prints the values within the first key
    for i in range (0, len(x)):
        temp = len(x.get(arr[i]))
        # outputs the number of indicies within the list of the value and name of the key in upper case
        print(str(temp) + " " + arr[i].upper())
        for j in range (0, temp):
            # Go over this, not 100% sure why it worked. why not print(x.get(arr[i][j])) -- does x.get(arr[i]) = the first index and the [j] alone represent the second? 
            print(x.get(arr[i])[j])
        print("")

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon