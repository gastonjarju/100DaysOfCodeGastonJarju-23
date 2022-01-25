
"""
This is a program that calculates a user's total restaurant bill and the tips they intend to give.
It can also split the bill among the number of people and return the total fo each individual.
"""


def userInput(firstName, lastName):
    """

    """
    if firstName == "" or lastName == "":
        return "You did not provide valid inputs"
    firstName = firstName.title()
    lastName = lastName.title()
    return f"Hey {firstName} {lastName}, welcome to the Tip Calculator\n"


def userTip(userTip):
    """

    """
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
    """
    """
# State and their Taxes
# https://taxfoundation.org/2021-sales-taxes/
    states = {
            "alabama": 9.22, "al": 9.22,
            "alaska": 1.76, "ak": 1.76,
            "arizona": 8.40, "ak": 8.40,
            "arkansas": 8.60, "ar": 8.60,
            "california": 9.51, "ca": 9.51,
            "colorado": 7.72, "co": 7.72,
            "delaware":  0.00,"de": 0.00,
            "district of columbia": 6.00, "dc": 6.00,
            "florida": 7.08, "fl": 7.08,
            "georgia": 7.32, "ga": 7.32,
            "hawaii": 4.44,  "hi": 4.44,
            "idaho": 6.03, "id": 6.03,
            "illinois": 8.82, "il": 8.82,
            "indiana": 7.00,  "in": 7.00,
            "iowa": 6.94, "ia": 6.94,
            "kansas": 8.69, "ks": 8.69,
            "kentucky": 8.7, "ky": 8.7,
            "louisiana": 9.52, "la":9.52,
            "maine": 5.50, "me": 5.50,
            "maryland": 6.00, "md": 6.00,
            "massachusetts": 6.25, "ma": 6.25,
            "michigan": 6.00, "mi": 6.00,
            "minnesota": 7.46, "mn":7.46,
            "mississippi": 7.07, "ms": 7.07,
            "missouri": 0.00, "mo": 0.00,
            "montana ": 9.22, "mt": 9.22,
            "Nebraska": 8.23, "ne": 8.23,
            "new hampshire": 0.00, "nh": 0.00,
            "new Jersey": 0.00, "nj": 0.00,
            "new mexico": 7.83, "nm": 7.83,
            "new york": 8.52, "ny": 8.52,
            "north Carolina": 6.98, "nc": 6.98,
            "north dakota": 6.96, "nd": 6.96,
            "ohio": 7.23, "oh": 7.23,
            "oklahoma": 8.95, "ok": 8.95,
            "oregon": 0.00, "or": 0.00,
            "pennsylvania": 6.34, "pa": 6.34,
            "rhode island": 7.00, "ri": 7.00,
            "south carolina": 7.46, "sc": 7.46,
            "south dakota": 6.40, "sd": 6.40,
            "tennessee": 9.55, "tn": 9.55,
            "texas": 8.19, "tx": 8.19,
            "utah": 7.19, "ut": 7.19,
            "vermont": 6.24, "vt": 6.24,
            "virginia": 5.73, "va": 5.73,
            "washington": 9.23, "wa": 9.23,
            "West Virginia": 6.50, "wv": 6.50,
            "wisconsin": 5.43, "wi": 5.43,
            "wyoming": 5.33, "wy": 5.33
    }
    state = state.lower()
    getStateTaxes = states[state]
    return getStateTaxes


def initialBill(billUntaxed, numberOfPeople):
    """

    """
    floatBillUntaxed = float(billUntaxed)
    intNumberOfPeople = int(numberOfPeople)
    billBeforeTipTax = floatBillUntaxed/intNumberOfPeople

    return billBeforeTipTax


def userCalculation(billBeforeTipTax,numberOfPeople,taxPercent,userTipPercent):
    """

    """
    # Debugging
    # initBill = initialBill(billBeforeTipTax,numberOfPeople)
    # taxP = taxPercent(taxPercent) # This is where the error is coming from.
    # tip = userTip(userTipPercent)
    # print(f"This is the billbefore, {billBeforeTipTax},taxP, {taxPercent}, tip, {tip}")
    totalBill = initialBill(billBeforeTipTax,numberOfPeople) * taxPercent * userTipPercent

    return f"Your total bill is {totalBill}"


def main():
    """

    """
    modifiedUserInput = userInput(input("Enter you first name:\n"), input("Enter your last name:\n"))
    print(modifiedUserInput)

    modifiedUserTip = userTip(input("How was the service? (Excellent(25% Tip), Good(15% Tip), Poor(5% Tip),"
                                       " Terrible(0% Tip) \n"))
    print(modifiedUserTip)

    modifiedTaxPercent = taxPercent(input("Enter the state you are in:\n"))
    print(modifiedTaxPercent)

    totalBill = float(input("What was the total bill?\n"))
    numberOfPeople = float(input("How many people to split the bill?\n"))

    modifiedInitialBill = initialBill(totalBill, numberOfPeople)

    print(modifiedInitialBill)

    modifiedTotalBill = userCalculation(modifiedInitialBill, numberOfPeople, modifiedTaxPercent, modifiedUserTip)
    print(modifiedTotalBill)


if __name__ == "__main__":
    main()



