
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
userName = input("What is your name?\n")
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
elif stateTax == "Alaska" or "alaska" or "ak" or "AK":
    taxPercent = 1.76
elif stateTax == "Arizona" or "arizona" or "AZ" or "az":
    taxPercent = 8.40
elif stateTax == "Arkansas" or "arkansas" or "AR" or "ar":
    taxPercent = 8.68
elif stateTax == "California" or "california" or "ca" or "CA":
    taxPercent = 9.51
elif stateTax == "Colorado" or "colorado" or "co" or "CO":
    taxPercent = 7.72
elif stateTax == "Connecticut" or "connecticut" or "CT" or "ct":
    taxPercent = 6.35
elif stateTax == "Delaware" or "delaware" or "de" or "DE":
    taxPercent = 0.00
elif stateTax == "District of Columbia" or "D.C" or "dc" or "DC":
    taxPercent = 6.00
elif stateTax == "Florida" or "florida" or "fl" or "FL":
    taxPercent = 7.08
elif stateTax == "Georgia" or "georgia" or "ga" or "GA":
    taxPercent = 	7.32
elif stateTax == "Hawaii" or "hawaii" or "hi" or "HI":
    taxPercent = 	4.44
elif stateTax == "Idaho" or "idaho" or "id" or "ID":
    taxPercent = 6.03
elif stateTax == "Illinois" or "illinois" or "il" or "IL":
    taxPercent = 8.82
elif stateTax == "Indiana" or "indiana" or "in" or "IN":
    taxPercent = 7.00
elif stateTax == "Iowa" or "Iowa" or "ia" or "IA":
    taxPercent = 6.94
elif stateTax == "Kansas" or "kansas" or "ks" or "KS":
    taxPercent = 	8.69
elif stateTax == "Kentucky" or "kentucky" or "ky" or "KY":
    taxPercent = 6.00
elif stateTax == "Louisiana" or "louisiana" or "la" or "LA":
    taxPercent = 9.52
elif stateTax == "Maine" or "Maine" or "me" or "ME":
    taxPercent = 5.50
elif stateTax == "Maryland" or "Maryland" or "md" or "MD":
    taxPercent = 6.00
elif stateTax == "Massachusetts" or "massachusetts" or "ma" or "MA":
    taxPercent = 6.25
elif stateTax == "Michigan" or "Michigan" or "mi" or "MI":
    taxPercent = 6.00
elif stateTax == "Minnesota" or "Minnesota" or "mn" or "MN":
    taxPercent = 7.46
elif stateTax == "Mississippi" or "mississippi" or "mo" or "MO":
    taxPercent = 7.07
elif stateTax == "Missouri" or "missouri" or "ky" or "KY":
    taxPercent = 0.00
elif stateTax == "Montana " or "montana " or "ky" or "MT":
    taxPercent = 9.22
elif stateTax == "Nebraska" or "Nebraska" or "ne" or "NE":
    taxPercent = 6.94
elif stateTax == "Nevada" or "nevada" or "ky" or "KY":
    taxPercent = 8.23
elif stateTax == "New Hampshire" or "new hampshire" or "nh" or "NH":
    taxPercent = 0.00
elif stateTax == "New Jersey" or "New Jersey" or "nj" or "NJ":
    taxPercent = 0.00
elif stateTax == "New Mexico" or "new mexico" or "nm" or "NM":
    taxPercent = 7.83
elif stateTax == "New York" or "new york" or "ny" or "NY":
    taxPercent = 8.52
elif stateTax == "North Carolina" or "North Carolina" or "nc" or "NC":
    taxPercent = 6.98
elif stateTax == "North Dakota" or "north dakota" or "nd" or "ND":
    taxPercent = 6.96
elif stateTax == "Ohio" or "ohio" or "oh" or "OH":
    taxPercent = 7.23
elif stateTax == "Oklahoma" or "oklahoma" or "ok" or "OK":
    taxPercent = 8.95
elif stateTax == "Oregon" or "oregon" or "or" or "OR":
    taxPercent = 0.00
elif stateTax == "Pennsylvania" or "pennsylvania" or "pa" or "PA":
    taxPercent = 6.34
elif stateTax == "Rhode Island" or "rhode Island" or "ky" or "KY":
    taxPercent = 7.00
elif stateTax == "South Carolina" or "South Carolina" or "sc" or "SC":
    taxPercent = 7.46
elif stateTax == "South Dakota" or "south dakota" or "sd" or "SD":
    taxPercent = 6.40
elif stateTax == "Tennessee" or "tennessee" or "tn" or "TN":
    taxPercent = 9.55
elif stateTax == "Texas	" or "texas	" or "tx" or "TX":
    taxPercent = 8.19
elif stateTax == "Utah" or "Utah" or "ut" or "UT":
    taxPercent = 7.19
elif stateTax == "Vermont" or "vermont" or "vt" or "VT":
    taxPercent = 6.24
elif stateTax == "Virginia " or "virginia " or "va" or "VA":
    taxPercent = 5.73
elif stateTax == "Washington" or "washington" or "wa" or "WA":
    taxPercent = 9.23
elif stateTax == "West Virginia" or "West Virginia" or "wv" or "WV":
    taxPercent = 6.50
elif stateTax == "Wisconsin" or "wisconsin" or "wi" or "WI":
    taxPercent = 5.43
elif stateTax == "Wyoming" or "wyoming" or "wy" or "WY":
    taxPercent = 5.33
else:
   print("INVALID STATE. Please insert a valid state.")