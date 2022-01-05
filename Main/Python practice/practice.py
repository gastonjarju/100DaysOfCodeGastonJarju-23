
"""
This is a program that calculates a user's total restaurant bill and the tips they intend to give.
It can also split the bill among the number of people and return the total fo each individual.
"""
print("!!!!!!!!!!!!!!-------------!!!!!!!!!!!!!!!!!!!!")
# Declaring variables
tenTip = 1.1
twelveTip = 1.12
fifteenTip = 1.15
# Calculation starts here
print("Welcome to the Tip Calculator!\n")
totalBill = (float(input("What was the total bill?\n $")))
totalBill = "{:.2f}".format(totalBill)
totalBill = float(totalBill)
print(totalBill)
userTip = int(input("How much tip percent would you like to give? 10, 12, 15 \n"))
numberOfPeople = int(input("How many people to split the bill? \n"))
if userTip == 10:
    userTotal = (totalBill /numberOfPeople) * tenTip
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay: {userTotal}')
elif userTip == 12:
    userTotal =  (totalBill /numberOfPeople) * twelveTip
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay: ${userTotal}')
else:
    userTotal =  (totalBill /numberOfPeople)  * fifteenTip
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay:{userTotal}')






