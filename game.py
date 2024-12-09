import hashlib

def length_check():
    while True:
        inp = input("Enter your password: ")
        if len(inp) < 8:
            print("Your password is too short. Please enter a password of at least 8 characters.")
        else:
            return inp


def create_sha1_hash(input_from_user):
    result = hashlib.sha1(input_from_user.encode()).hexdigest()
    return result


checked_input = length_check()
hashed_result = create_sha1_hash(checked_input)
print('Your hashed password is: ', hashed_result)
