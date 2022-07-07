# Basic - Print all integers from 0 to 150.
    # 151 means less than 151, therefore 150
print("Start 1st problem")
for i in range (0,151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Start 2nd problem")
for j in range (5,1000, 5):
    print(j)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("Start 3rd problem")
for a in range (1,100):
    if(a % 10 == 0):
        print("Coding Dojo")
    elif(a % 5 == 0):
        print("Coding")
    else:
        print(a)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print("Start 4th problem")
sum = 0
for b in range (0, 500000):
    if(b % 2 == 1):
        sum += b
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print("Start 5th problem")
for c in range (2018, 0, -4):
    print(c)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("Start 6th problem")
lowNum = 2
highNum = 9
mult = 3
# the + 1 on the end of highnum is due ot the exlcusive stop, and in order to output the prompt, a 1 must be added.
for d in range (lowNum, highNum + 1):
    if(d % mult == 0):
        print(d)