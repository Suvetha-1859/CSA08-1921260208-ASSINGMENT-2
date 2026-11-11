import random

LOCK_MESSAGE = "Account locked for 30 minutes"


def send_otp():
    otp = str(random.randint(1000, 9999))
    print("OTP sent to your mobile (demo, shown here):", otp)
    return otp


# Design 1: while loop
def verify_while():
    otp = send_otp()
    attempts = 0
    while attempts < 3:
        entry = input("Enter OTP: ").strip()
        if entry == "":
            print("Blank entry - not counted")
            continue                          # counter not updated
        if entry == otp:
            print("OTP verified")
            break                             # success, skip the else
        attempts += 1                         # counts only a wrong entry
        print(f"Wrong OTP. Attempts used: {attempts}/3")
        if attempts < 3:
            pass                              # nothing extra, try again
    else:
        print(LOCK_MESSAGE)                   # runs only if no break


# Design 2: for loop with range(3)
def verify_for():
    otp = send_otp()
    for attempt in range(1, 4):
        while True:                           # keep asking until non-blank
            entry = input("Enter OTP: ").strip()
            if entry == "":
                print("Blank entry - not counted")
                continue
            break
        if entry == otp:
            print("OTP verified")
            break
        print(f"Wrong OTP. Attempts used: {attempt}/3")
    else:
        print(LOCK_MESSAGE)


# Changed condition: 2 extra attempts after a correct security answer
def verify_extended():
    otp = send_otp()
    attempts = 0
    max_attempts = 3
    security_asked = False
    while attempts < max_attempts:
        entry = input("Enter OTP: ").strip()
        if entry == "":
            print("Blank entry - not counted")
            continue
        if entry == otp:
            print("OTP verified")
            break
        attempts += 1
        print(f"Wrong OTP. Attempts used: {attempts}/{max_attempts}")
        if attempts == 3 and not security_asked:
            security_asked = True
            answer = input("Security question - your city of birth? ").strip().lower()
            if answer == "chennai":           # demo answer
                max_attempts = 5
                print("Correct. You get 2 extra attempts.")
    else:
        print(LOCK_MESSAGE)


# Alternative: recursion
def verify_recursive(otp, attempt=1):
    if attempt > 3:
        print(LOCK_MESSAGE)
        return
    entry = input("Enter OTP: ").strip()
    if entry == "":
        print("Blank entry - not counted")
        verify_recursive(otp, attempt)        # same attempt number
    elif entry == otp:
        print("OTP verified")
    else:
        print(f"Wrong OTP. Attempts used: {attempt}/3")
        verify_recursive(otp, attempt + 1)


print("1. while loop")
print("2. for loop (range 3)")
print("3. changed condition (2 extra attempts)")
print("4. recursive version")
choice = input("Choose 1-4: ").strip()

if choice == "1":
    verify_while()
elif choice == "2":
    verify_for()
elif choice == "3":
    verify_extended()
elif choice == "4":
    verify_recursive(send_otp())
else:
    print("Invalid choice")
