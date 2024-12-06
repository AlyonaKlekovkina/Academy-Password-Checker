def length_check():
    while True:
        inp = input("Enter your password: ")
        if len(inp) < 8:
            print("Your password is too short. Please enter a password of at least 8 characters.")
        else:
            return "You entered:  ", inp

print(length_check())

