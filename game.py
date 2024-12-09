import hashlib
import requests


def length_check():
    while True:
        inp = input("Enter your password: ")
        if len(inp) < 8:
            print("Your password is too short. Please enter a password of at least 8 characters.")
        else:
            return inp


def create_sha1_hash(input_from_user):
    return hashlib.sha1(input_from_user.encode()).hexdigest()


def send_request(full_hashed_password):
    first_five_chars = full_hashed_password[:5]
    address = 'https://api.pwnedpasswords.com/range/{}'.format(first_five_chars)
    #response = requests.get(address)
    return address


checked_input = length_check()
hashed_result = create_sha1_hash(checked_input)
print('Your hashed password is: ', hashed_result)
print('Checking...')
print('A request was sent to ')
full_address = send_request(hashed_result)
print('"{}"'.format(full_address))
print('endpoint, awaiting response...')
