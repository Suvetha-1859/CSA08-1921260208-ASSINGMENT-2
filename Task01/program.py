units = int(input("Enter electricity units: "))
ration = input("Do you have ration card? (yes/no): ").lower()
age = int(input("Enter age of oldest member: "))

if units <= 100:
    print("Full subsidy")

elif units <= 200:
    if ration == "yes":
        print("Partial subsidy")
    else:
        print("No subsidy")

else:
    if age > 80:
        print("Senior citizen exception")
    else:
        print("No subsidy")
