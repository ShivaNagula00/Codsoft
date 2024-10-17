import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lower + upper + digits + special
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    length = int(input())
    password = generate_password(length)
    print(password)

main()
