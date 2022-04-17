"""
ex_1 = False
ex_2 = 29
ex_3 = 4.1352

print(type(ex_1))
print(type(ex_2))
print(type(ex_3))

ex_4 = str(False)
ex_5 = str(29)
ex_6 = str(4.1352)

print(type(ex_4))
print(type(ex_5))
print(type(ex_6))

#######
import numpy as np

intVal = 5

floatVal = 2.21

boolVal = False

print(boolVal)

boolVal = True

print(intVal)

print(floatVal)

print(boolVal)

l = [1, 2]
nplist = np.array(l)
print(nplist)

################################
diego = 'diego likes the gym.'
print(diego[3:8])
###
print("cars"[0])
###
concatenated = "R2" + "-" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])
###
unchanged = "forest gump"
sliced = unchanged[:6]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)

#############

# The \t gives a extra space between the words.

print("My\tcar\tis\ttoo\tbig")

# The \n divides the phase.
print("My\ncar\nis\ntoo\nbig")

# The \" add quotes to the phase.

print("\"Mycar is too big\"")

# The double back-slash(\\) can be used for adding slash in any part o the phase.

print("Mycar is too big\\.")

# Exercise.

print("*******\n ***** \n  ***  \n   *  ")

#name = input("Please enter your name.")
#print("Your name is " + name + ".")
#print(type(name))

#fav_num = input("Please enter your favorite number?")
#print("Your favorite number is " + fav_num + ".")
#print(type(fav_num))

#guest = input("Please enter your guest name?")
#print("Your guest name is " + guest + ".")
#print(type(guest))

#print(("Your guest name is " + guest + "."), ("Your favorite number is " + fav_num + "."), ("Your name is " + name + "."))

#How will you verify if the items present in list A are present in series B? We will use the isin() function. For this, we create two series s1 and s2 –

import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
s3 = s1[s1.isin(s2)]
print(s3)

#How to find the positions of numbers that are multiples of 4 from a series? For finding the multples of 4, we will use the argwhere() function. First, we will create a list of 10 numbers –

#s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#np.argwhere(ser % 4==0)

#Can you stack two series horizontally? If so, how?Yes, we can stack the two series horizontally using concat() function and setting axis = 1.
df = pd.concat([s1, s2], axis=1)
print(df)

#How can you convert date-strings to timeseries in a series?
#Input:

s = pd.Series(['02 Feb 2011', '02-02-2013', '20160104', '2011/01/04', '2014-12-05', '2010-06-06T12:05'])

#To solve this, we will use the to_datetime() function.

print(pd.to_datetime(s))

# print as many times

def prints_four():
    print("I love corsa gsi")
    print("I love corsa gsi")
    print("I love corsa gsi")
    print("I love corsa gsi")

prints_four()
prints_four()

# function
def function_name():
    print(2 + 2)

function_name()

#fuction and paramenter
def function_name(parameter):
    print(parameter + 2)
function_name(8)

#fuction and paramenter ex 2

first_str = "The number "
def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)

function_name(first_str, 5, " is an integer")

user_int = int(input("Please enter an integer:"))
print(user_int)
print(type(user_int))

user_float = float(input("Please enter the float:"))
print(user_float)
print((type(user_float)))

# import function
import random
print(random.randint(1, 10))

# import model from a function
from random import randint
print(randint(10, 20))

# universal import
from random import *
print(random())

# Create a global variable scope
example = "I like dogs" # global variable scope

# Create a local variable scope
def diego_func():
    example = "corsa gsi are the best" # local variable scope
    return example

# Print global and local scope
print(example) # global variable scope
print(diego_func()) # local variable scope


# Create a function that will print the variable created: "example"
def diego_func():
    print(example)

example = "corsa gsi are the best" # local variable scope

diego_func() # This will print the all function without using the print code

# This function join two variable functions:
def print_strings():
    diego = " and cats "
    print(example + diego)

print_strings() # This will print the all function without using the print code

# This function show how to change variables in the function using the "global" function:

# First Create a function
def diego_new():
    fruit = "apple"
    print(fruit)

# Create a second function, but now add the global function inside the function to change the global variable "fruit" below:
def diego_new1():
    #global fruit
    fruit = "banana"
    print(fruit)

fruit = "pinaple" # global variable fruit

diego_new()
diego_new1()
print(fruit)



# Python lets print some positive codes:

people = "  Coronavirus "

corona_virus = "will be over soon"
win = " and the world will be fine again."
love = " 'Don't worry about a thing, cause every little thing gonna be all right'."
together = "  Thank you NHS. "

print(people + corona_virus + win)
print(love)
print(together)

###

# Create a Global variable and join with a local variable.
def test ():
    like = "I chicken burger"
    print(like + no)

# Create a local variable.
no = " but I don't like coke"

test()

###

# Create a Global variable and join with a local variable.
def test ():
    like = "I chicken burger"
    return(like + no)

# Create a local variable.
no = " but I don't like coke"

print(test())

###

#Flow control steatments

print(1 == 2) #equal
print(2 != 1) #not equal
print(2 < 1) #smaller
print(2 > 1) #bigger

#Example:
# The "and" statement
print(4 > 1 and "word" == "word") # True and True
print(7 == 5 and 2 != 4) #False and True
print(52 != 50 and "corsa gsi" == "Corsa gsi") #True and False
print(45 > 30 and "Corsa gsi" == "Corsa gsi") #True and True

# The "or" statement

print(4 > 1 or "word" == "word") # True and True
print(7 == 5 or 2 != 4) #False and True
print(52 != 50 or "corsa gsi" == "Corsa gsi") #True and False
print(45 > 30 or "Corsa gsi" == "Corsa gsi") #True and True
print(100 < 30 or "Corsa gsi" == "corsa gsi") #False and False

# The "not" statement

print(not 1 == 2) #equal
print(not 2 != 1) #not equal
print(not 2 < 1) #smaller
print(not 2 > 1) #bigger

###

# The "if" statements, this can be applied to (!=), (<), (>), (or), (and).

car = input("what color is your car:")

if car == "red":
    print("The car is red.")

# Otherwise the "else" statements

if car == "red":
    print("The car is red.")

else:
    print("The has the wrong color.")

###

# Create a more complicated statement

customer = float(input("What is the customer rating?"))
rating = input("This customer has a good rating?")

if customer >= 5.0:
    if rating == "no":
        print("Unfortunately the customer did not match the minimum requirement")
    else:
        print("Yes, the customer has a great rating.")
else:
    print("The minimum rating requirement is 5.0")

###

# Exercise
score = int(input("Please enter the student's score. "))

if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    else:
        if score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        else:
            if score >= 60:
                print("This student's score of " + str(score) + " is a D.")
            else:
                print("This student's score of " + str(score) + " is a F.")

###

# elif statement

user_num = int(input("Please enter an integer:"))

if user_num < 0:
    print("The number you entered is less than 0")
elif user_num == 0:
    print("The number you entered is 0")
elif user_num <= 100:
    print("The number you entered can be 1, 100, or anything in between.")
else:
    print("The number you entered is greater than 100.")

###

# Roman Numerical Equivalent Solution

from random import randint

one_to_ten = randint(1, 10)

if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")


 # Truth or False condiction:

string_ex = input("Enter a string:")

if string_ex:
    print("Thank you for entering a string.")
else:
    print("You did not enter a string.")

###

# While Loop Tutorial

counter = 0

while counter < 5: # counter the number all the way to number 5
    print("Something") # counter "Something" all the way to number 5
    counter += 1  #Condiction applied that applies the count Ex 0+1= 1, 1+1=2, 2+1=3 .... =5 (the end of the loop)

###

# Complex example:

# pos_int is a variable which holds a user entered integer.
pos_int = int(input("Please enter a positive integer:"))
# This variable stores the initial value of pos_int before it is used in the loop so
# that later it can be used to display pos_int's initial value in the output.
int_init = pos_int
# This is a variable which will be used to hold the sum of all the integers from pos_int.
summed = 0
# The while loop will run while pos_int's stored integer value is greater than 0
while pos_int > 0:
    # This is the equivalent of summed = summed + pos_int
    # In other words: new value of summed = old value of summed + new value of pos_int
    summed += pos_int
    # This will decrement pos_int so that pos_int will eventually equal 0 and the while
    # loop will stop running its code.
    pos_int -= 1

print(int_init)  # displays the initial value of pos_int
print(summed)  # displays the sum of integers from pos_int

###

# For loop with strings: print each letter in the loop

word = "house"

for letter in word:
    print(letter)
###

# Find The Number of Characters in A String Solution
user_str = input("Please enter a string:")

count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1

print(user_str)
print(count)

###

# Range values: 1, 2, 3 .... 5.

one_input = range(5)

for num in one_input:
    print(num)

# Range with two input values: 5, 6, 7 ....10

two_inputs = range(5, 10)

for num in two_inputs:
    print(num)

# Increment Range with three input values: 9, 7, 5, 3 and 1.

three_inputs = range(1, 10, 2)

for num in three_inputs:
    print(num)

# Down up Range with three input values: 1, 3, 5, 7 and 9.

three_inputs = range(10, 11, 2)

for num in three_inputs:
    print(num)

# Exercise 1

# Write a program that prints the integers 1 through 50 using a loop.
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
# For numbers which are multiples of 3 but not 5 print “Fizz” instead of the number and for the numbers that are multiples of 5 but not 3 print “Buzz” instead of the number.
# All of the remaining numbers which are not multiples of 3 or 5 should just be printed as themselves.

for num in range(1, 51):
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If num is only divisible by 3, "Fizz" will be printed.
    elif num % 3 == 0:
        print("Fizz")
    # If num is only divisible by 5, "Buzz" will be printed.
    elif num % 5 == 0:
        print("Buzz")
    # num itself will be printed in all other cases.
    else:
        print(num)


# Exercise 2

# Create a function which takes one positive integer as its input and returns its factorial.
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls.
# For those inputs, you should get 6, 24, and 120, respectively.

# The argument fac_num's name is short for factorial number.
def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item

    # returns returned, which now holds the value of fac_num's factorial
    return returned


print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120

####
# Lower case or hipper case.

all_low = "the dog is very small"
print(all_low.upper())

all_upper = "THE DOG IS VERY BIG"
print(all_upper.lower())

# Is lower or is upper
print("I LIKE DOGS".isupper())
print("i like dogs is lower".isupper())

print("I LIKE DOGS".islower())
print("i like dogs is lower".islower())

# Combine is and upper or lower.
print("the car is broken".upper().islower())

# Print the string in lower case and confirm is working.
print("DOG".lower().isupper())

# Print .isalpha() = only letters and no mumber.
print("DOG".lower().isalpha())

print("DOG2".lower().isalpha())

#Is noum? String with letter and number.
print("Batman12".isalnum())
print("Batman".isalnum())

#Is decimal
print("123".isdecimal())
print("Batman123".isdecimal())

#Is space?
print("".isspace())
print("   ".isspace())
print("Hot dog".isspace())
print("Hotdog is cold"[6].isspace())

#Is title?
print("The Empire Strickes Back".istitle())

#Turn to title:
print("romeo and juliete".title())

#Start with:
print("this is a string".startswith("this"))

#Ends with:
print("To infnity and beyond!".endswith("beyond!"))

#Join methodo:
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print(" dog ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))

#The split:
print("Eggs, Milk, Waffles, Bacon".split(","))
print("Eggs, Milk, Waffles, Bacon".split(", "))

# Adding spaces to the left or to the right:
#To the right:
print("hello world".rjust(15))
#To the left:
print("hello world".ljust(15))
#Ex:

print("hello world".ljust(15) + "I am here")
print("hello world".rjust(15) + "I am here")

# Center the strings:
print("hello world".center(15, ":"))
print("hello world".center(15))

# Strip method, removes letters from strings.
print("My dog likes playing along!!! 22222")
print("My dog likes playing along!!! 22222".strip("2"))
print("My dog likes playing along!!! 22222".rstrip("2"))
print("My dog likes playing along!!! 22222".lstrip("M"))
print("My dog likes playing along!!! 22222".lstrip("My"))
print("My dog likes playing along!!! 22222".rstrip("22222"))
print("My dog likes playing along".rstrip("along"))
print("My dog likes playing along".strip("along"))

#Replacing argument:
print("My dog likes playing along".replace("along", "together"))

# Count hte length of a string:
dog = "I like dogs"
print(len(dog))
print(len("the big dog"))

#Example, how to reverse a string in python?
user_string = input("Please enter a string:")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)

#Example: count the words in the text rom Forest Gump.

str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in str_1:
    if char.isalnum() or char.isspace() or char == "-":
        spaces_and_letters += char

words = spaces_and_letters.split()
number_of_words = len(words)

print(words)
print(number_of_words)

# Format method for Strings:
name = input("Applicant name:")
degree = input("Degree:")
job = input("Occupation:")
experience = input("How many years of experience:")
print(name + " is majored in " + degree + ", works as a " + job + ", and has " + experience + " years of experience.")

# Using Format: using.format()
name = input("Applicant name:")
degree = input("Degree:")
job = input("Occupation:")
experience = input("How many years of experience:")
print("{} is majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))

# List Introduction:
example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = ["green", "blue", "orange", "pink", "yellow"]
example_list_3 = [["green", "blue", "orange", "pink", "yellow"], [5, 4, 3, 2, 1]]
print(example_list_3)

# Print "blah" as a list.
print(list("blah"))

# The in and not in operators, check if certain values are in the operator:
check_list = [1, 2, 3, 4]
print(1 in check_list)
# Lets check another value, ex: 8?
print(8 in check_list)
#use a different approach:
not_in_the_example = 8 not in check_list
print(not_in_the_example)

# Access index from an item index in a list "[]":
indexes_example = ["corsa", "fiat", "ford"]
print(indexes_example[1])

#Select the index rom a list:
indexes_example = [[1, 2, 3], [4, 5, 7], ["dod", "cat", "horse"]]
print(indexes_example[2] [2])
#Select the index rom a list from the order side using negative value:
negative = [1, 2, 3, 4, 5, 7, "dod", "cat", "horse"]
print(negative[-2])

# Using index values or mulples expressions, ex maths and strings:
mixed = [1, 2, 3, 4, 5, 7, "dod", "cat", "horse"]
print(mixed[3] + 5)
print("I have two \"" + mixed[-1] + "\" in my farm.")

# List slice:
sliced = [1, 2, 3, 4, 5, 7, "dod", "cat", "horse"]
print(sliced[:6])
print(sliced[3:6])
print(sliced[6:])

# Replace the value from the index:
replace = [1, 2, 3, 4, 5, 7, "dod", "cat", "horse"]
print(replace)
replace[-2] = "bird"
print(replace)

#Delete items rom a string:
planet = ["pluto", "mars", "earth", "venus"]
del planet[0]
print(planet)

#Remove method:
planet = ["pluto", "mars", "earth", "venus"]
planet.remove("mars")
print(planet)

#How to remove multiple repetitive items from a string, only the first find item will be removed:
planet = ["pluto", "mars", "earth", "venus","pluto","pluto","pluto","pluto"]
planet.remove("pluto")
print(planet)

#Append method:
planet = ["pluto", "mars", "earth", "venus"]
planet.append("saturn")
print(planet)

#Assign item to a string, insert to specific location:
planet = ["pluto", "mars", "earth", "venus"]
planet.insert(2,"saturn") #notice that saturn will appear in the second place from the string.
print(planet)

#Sort method will add order to the numbers:
list_numbers = ["1.2", "-3.4", "100", "24", "0"]
print(list_numbers)
list_numbers.sort()
print(list_numbers)

beattles = ["Ringo", "John", "George", "Paul"]
print(beattles)
beattles.sort()
print(beattles)

# The reverse method can be added to the string and the sort items will be sorted in the other way:
list_numbers = ["1.2", "-3.4", "100", "24", "0"]
print(list_numbers)
list_numbers.sort(reverse=True)
print(list_numbers)

beattles = ["Ringo", "John", "George", "Paul"]
print(beattles)
beattles.sort(reverse=True)
print(beattles)

#Strings in alphabetics orders have one rule, the capital letters will come first:
Alphabetic = ["dog", "cat", "Horse", "Bird", "Cow"]
Alphabetic.sort()
print(Alphabetic)

#Parse the string to be includ Capital letter and lower letts in the sort fucting:
Alphabetic = ["dog", "cat", "Horse", "Bird", "Cow"]
Alphabetic.sort(key=str.lower)
print(Alphabetic)

#Find the index number of the string:
find_index = ["dog", "cat", "Horse", "Bird", "Cow"]
print(find_index.index("Bird"))

#Pop method removes and return the items from a list:
band = ["The Beatllers", "Queen", "Led Zeppelin", "Muse", "Radiohead"]
end = band.pop()
print(band)
print(end)

#Print item 3 from the pop methond:
band = ["The Beatllers", "Queen", "Led Zeppelin", "Muse", "Radiohead"]
end = band.pop(3)
print(band)
print(end)

"""