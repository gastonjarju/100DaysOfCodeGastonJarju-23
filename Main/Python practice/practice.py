
# Function Practice
# def userName():
#     name = input("What is your name?")
#     if name == "Gaston":
#         print("Keep up the great job")
#     else:
#         print("Try next time!")
#     return name
#
# userName()

# 100DAYS OF CODING CHALLENGE
# DAY 9:

"""
You are going to write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
Line 8 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as name followed by comma then space. e.g. Angela, Ben, Jenny, Michael, Chloe
"""

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
# 🚨 Don't change the code above 👆

random_index = random.randint(0, len(names)-1)
random_name = names[random_index]
print(f" {random_name} is going to buy the meal today!")

