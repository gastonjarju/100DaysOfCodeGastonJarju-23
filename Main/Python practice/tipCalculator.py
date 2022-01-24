
"""
This is a program that calculates a user's total restaurant bill and the tips they intend to give.
It can also split the bill among the number of people and return the total fo each individual.
"""


def userInput(firstName, lastName):
    if firstName == "" or lastName == "":
        return "You did not provide valid inputs"
    firstName = firstName.title()
    lastName = lastName.title()
    return f"Hey {firstName} {lastName}, welcome to the Tip Calculator\n"



def userTip(userTip):
    if userTip == "Excellent" or "excellent":
        userTipPercent = 0.25
    elif userTip == "Good" or "good":
        userTipPercent = 0.15
    elif userTip == "Poor" or "poor":
        userTipPercent = 0.10
    elif userTip == "Terrible" or "terrible":
        userTipPercent = 0
    else:
        print("INVALID INPUT. Please insert a valid service rating \n")
    return userTipPercent



def taxPercent(state):
# State and their Taxes
# https://taxfoundation.org/2021-sales-taxes/
#     print("We have reached to this function")
    state = state.lower()
    states = {"alabama": 9.22,"al":9.22,'kentucky':8.7,"ky":8.7}
    getStateTaxes = states[state]

    # if stateTax == "Alabama" or "alabama" or "al" or "AL":
    #     taxPercent = 9.22
    # elif stateTax == "Alaska" or "alaska" or "ak" or "AK":
    #     taxPercent = 1.76
    # elif stateTax == "Arizona" or "arizona" or "AZ" or "az":
    #     taxPercent = 8.40
    # elif stateTax == "Arkansas" or "arkansas" or "AR" or "ar":
    #     taxPercent = 8.68
    # else:
    #     print("INVALID INPUT. Please insert a valid service rating \n")

    return getStateTaxes


def initialBill(billUntaxed, numberOfPeople):
    floatBillUntaxed = float(billUntaxed)
    intNumberOfPeople = int(numberOfPeople)
    billBeforeTipTax = floatBillUntaxed/intNumberOfPeople

    return billBeforeTipTax


def userCalculation(billBeforeTipTax,numberOfPeople,taxPercent,userTipPercent):
    # initBill = initialBill(billBeforeTipTax,numberOfPeople)
    # taxP = taxPercent(taxPercent) # This is where the error is coming from.
    # tip = userTip(userTipPercent)
    # print(f"This is the billbefore, {billBeforeTipTax},taxP, {taxPercent}, tip, {tip}")
    totalBill = initialBill(billBeforeTipTax,numberOfPeople) * taxPercent  * userTipPercent

    return f"Your total bill is {totalBill}"



def main():
    modifiedUserInput= userInput(input("Enter you first name:\n"), input("Enter your last name:\n"))
    print(modifiedUserInput)

    modifieduserTip = userTip(input("How was the service? (Excellent(25% Tip), Good(15% Tip), Poor(5% Tip),"
                                       " Terrible(0% Tip) \n"))
    print(modifieduserTip)

    modifiedtaxPercent = taxPercent(input("Enter the state you are in:\n"))
    print(modifiedtaxPercent)

    totalBill = float(input("What was the total bill?"))
    numberOfPeople =  float(input("How many people to split the bill?"))

    modifiedInitialBill = initialBill(totalBill,numberOfPeople)

    print(modifiedInitialBill)

    modifiedTotalBill = userCalculation(modifiedInitialBill,numberOfPeople,modifiedtaxPercent,modifieduserTip)
    print(modifiedTotalBill)


if __name__ == "__main__":
    main()



