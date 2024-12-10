import hashlib
import requests
import re
import sys


def length_check(input_string):
    while True:
        if len(input_string) < 8:
            print("Your password is too short. Please enter a password of at least 8 characters.")
        else:
            return input_string


def create_sha1_hash(input_from_user):
    return hashlib.sha1(input_from_user.encode()).hexdigest()


def send_request(full_hashed_password):
    first_five_chars = full_hashed_password[:5]
    address = 'https://api.pwnedpasswords.com/range/{}'.format(first_five_chars)
    response = requests.get(address)
    last_chars = full_hashed_password[5:]
    full_response = response.text
    s = re.split(r"[~\r\n]+", full_response)
    for i in s:
        if last_chars in i.lower():
            result = i.split(':')
            return result[1]


while True:
    inp = input("Enter your password (or 'exit' to quit): ")
    args = sys.argv

    if inp == 'exit':
        print("Goodbye!")
        break
    else:
        checked_input = length_check(inp)
        hashed_result = create_sha1_hash(checked_input)
        if '--show-hash' in args:
            print('Your hashed password is: ', hashed_result)
        print('Checking...')
        resp = send_request(hashed_result)
        message = 'Your password has been pwned! The password "{}" appears {} times in data breaches.'.format(checked_input, resp)
        if resp is None:
            print("Good news! Your password hasn't been pwned.")
        else:
            print(message)
