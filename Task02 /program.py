OTP = "246810"

print("WHILE LOOP")
attempt = 0

while attempt < 3:
    entered = input("Enter OTP: ").strip()

    if entered == "":
        print("Blank entry - try again")
        continue

    attempt += 1

    if entered == OTP:
        print("Verified")
        break

    print("Wrong OTP")

else:
    print("Account locked for 30 minutes")


print("\nFOR LOOP")

for i in range(3):
    entered = input("Enter OTP: ").strip()

    while entered == "":
        print("Blank entry - not counted")
        entered = input("Enter OTP: ").strip()

    if entered == OTP:
        print("Verified")
        break

    print("Wrong OTP")

else:
    print("Account locked for 30 minutes")


# Example of pass
if False:
    pass
