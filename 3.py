province = {"A": "Newfoundland", "B":"Nova Scotia", "C":"Prince Edward Island",
                "E":"New Brunswick", "G":"Quebec", "H":"Quebec", "J":"Quebec",
                "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario",
                "P":"Ontario", "R":"Manitoba", "S":"Saskatchewan", "T":"Alberta",
                "V":"British Columbia", "X":"Nunavut", "X":"Northwest Territories", "Y":"Yukon"}
postalCode = input()

if len(postalCode) < 6 or postalCode[0] not in province.keys():
    print("invaid code")

else:
    print(f"province is {province[postalCode[0]]}")
    
    if postalCode[3] == "0": 
        print("place is rural")

    else:
        print("place is urban")