
"""
This is a program that calculates a user's total restaurant bill and the tips they intend to give.
It can also split the bill among the number of people and return the total fo each individual.
"""
print("!!!!!!!!!!!!!!-------------!!!!!!!!!!!!!!!!!!!!")
# # Declaring Tips variables
excellentService = 1.25
goodService = 1.15
poorService= 1.05
terribleService = 1

# # Calculation starts here
print("Welcome to the Tip Calculator!\n")
userName = input("What is your name:\n")
totalBill = (float(input("What was the total bill?\n $")))
totalBill = "{:.2f}".format(totalBill)
totalBill = float(totalBill)
# State Taxes
stateTax = input("Enter the state you are in:\n")
userTip = input("How was the service? (Excellent(25% Tip), Good(15% Tip), Poor(5% Tip), Terrible(0% Tip) \n")
numberOfPeople = int(input("How many people to split the bill? \n"))
if userTip == "Excellent" or "excellent":
    userTotal = (totalBill /numberOfPeople) * excellentService
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay ${userTotal} before tax \n')
elif userTip == "Good" or "good":
    userTotal =  (totalBill /numberOfPeople) * goodService
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay ${userTotal} before tax \n')

elif userTip == "Poor" or "poor":
    userTotal = (totalBill / numberOfPeople) * poorService
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay ${userTotal} before tax \n')

elif userTip == "Terrible" or "terrible":
    userTotal = (totalBill / numberOfPeople) * terribleService
    userTotal = "{:.2f}".format(userTotal)
    print(f'Each person should pay ${userTotal} before tax \n')

else:
    print("INVALID INPUT. Please insert a valid service rating \n")

# State and their Taxes
# https://taxfoundation.org/2021-sales-taxes/
if stateTax == "Alabama" or "alabama" or "al" or "AL":
    taxPercent = 9.22
elif stateTax == "Kentucky" or "kentucky" or "ky" or "KY":
    taxPercent = 9.22
elif stateTax == "Kentucky" or "kentucky" or "ky" or "KY":
    taxPercent = 9.22
elif stateTax == "Kentucky" or "kentucky" or "ky" or "KY":
    taxPercent = 9.22
elif stateTax == "Kentucky" or "kentucky" or "ky" or "KY":
    taxPercent = 9.22
elif stateTax == "Kentucky" or "kentucky" or "ky" or "KY":
    taxPercent = 9.22
