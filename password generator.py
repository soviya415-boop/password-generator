import random
import string

def generate_password(length, upper, lower, digits, symbols):

    characters = ""

    if upper:
        characters += string.ascii_uppercase

    if lower:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if len(characters) == 0:
        return None

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def password_strength(password):

    score = 0

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


while True:

    print("\n======================================")
    print("      ADVANCED PASSWORD GENERATOR")
    print("======================================")
    print("1. Generate Password")
    print("2. Exit")
    print("======================================")

    choice = input("Enter Your Choice: ")

    try:

        if choice == "1":

            length = int(input("Enter Password Length: "))

            if length <= 0:
                raise ValueError("Password length must be greater than 0")

            upper = input("Include Uppercase Letters (yes/no): ").lower() == "yes"
            lower = input("Include Lowercase Letters (yes/no): ").lower() == "yes"
            digits = input("Include Numbers (yes/no): ").lower() == "yes"
            symbols = input("Include Symbols (yes/no): ").lower() == "yes"

            password = generate_password(
                length,
                upper,
                lower,
                digits,
                symbols
            )

            if password is None:
                print("Error: Select at least one character type.")
                continue

            print("\nGenerated Password :", password)
            print("Password Strength  :", password_strength(password))

        elif choice == "2":
            print("Thank You for Using Password Generator!")
            break

        else:
            print("Invalid Choice! Please Enter 1 or 2.")

    except ValueError as ve:
        print("Value Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)
