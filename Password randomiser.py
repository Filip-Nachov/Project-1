import string
import random

# list to store all our data
lc_letters = list(string.ascii_lowercase)
uc_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
special_digits = list(string.punctuation)

while True:
    characters_sum = input("How many characters do you want to be in your password: ")

    try:
        characters_number = int(characters_sum)

        if characters_number < 5:
            print('Your password length should be at least 5 characters.')
        else:
            print("Password length accepted:", characters_number)

            # Now, let's ask for the number of uppercase letters
            while True:
                uc_lett_length = input("How many uppercase letters do you want to be in your password: ")

                try:
                    uc_length = int(uc_lett_length)

                    if uc_length > characters_number:
                        print("Error: Uppercase letters length cannot be greater than the total characters.")
                    elif uc_length < 0:
                        print("Error: Uppercase letters length cannot be negative.")
                    else:
                        # Store uc_length in uc_letters
                        uc_letters = uc_letters[:uc_length]
                        random.shuffle(uc_letters)
                        break  # Break out of the loop if the input is a valid integer.

                except ValueError:
                    print("Please enter a valid number.")

            # Now, let's ask for the number of lowercase letters
            while True:
                lc_lett_length = input("How many lowercase letters do you want to be in your password: ")

                try:
                    lc_length = int(lc_lett_length)

                    if lc_length > characters_number - len(uc_letters):
                        print("Error: Lowercase letters length cannot be greater than the remaining characters.")
                    elif lc_length < 0:
                        print("Error: Lowercase letters length cannot be negative.")
                    else:
                        # Store lc_length in lc_letters
                        lc_letters = lc_letters[:lc_length]
                        random.shuffle(lc_letters)
                        break  # Break out of the loop if the input is a valid integer.

                except ValueError:
                    print("Please enter a valid number.")

            # Now, let's ask for the number of digits
            while True:
                num_lett_length = input("How many digits do you want to be in your password: ")

                try:
                    num_length = int(num_lett_length)

                    if num_length > characters_number - len(uc_letters) - len(lc_letters):
                        print("Error: Digits length cannot be greater than the remaining characters.")
                    elif num_length < 0:
                        print("Error: Digits length cannot be negative.")
                    else:
                        # Store num_length in numbers
                        numbers = numbers[:num_length]
                        random.shuffle(numbers)
                        break  # Break out of the loop if the input is a valid integer.

                except ValueError:
                    print("Please enter a valid number.")

            # Now, let's ask for the number of special digits
            while True:
                spd_lett_length = input("How many special digits do you want to be in your password: ")

                try:
                    spd_length = int(spd_lett_length)

                    if spd_length > characters_number - len(uc_letters) - len(lc_letters) - len(numbers):
                        print("Error: Special digits length cannot be greater than the remaining characters.")
                    elif spd_length < 0:
                        print("Error: Special digits length cannot be negative.")
                    else:
                        # Store spd_length in special_digits
                        special_digits = special_digits[:spd_length]
                        random.shuffle(special_digits)
                        break  # Break out of the loop if the input is a valid integer.

                except ValueError:
                    print("Please enter a valid number.")

            # Concatenate and shuffle all the lists
            all_characters = uc_letters + lc_letters + numbers + special_digits
            random.shuffle(all_characters)

            # Ensure the length of the password does not exceed characters_sum
            password_length = min(characters_number, len(all_characters))

            # Create the password using random.sample
            password = ''.join(random.sample(all_characters, password_length))

            # Display the password
            print("Password:", password)

            # Ask if the user wants to enter another password
            while True:
                another_password = input("Do you want to enter another password? (y/n): ").lower()

                if another_password == 'y':
                    break  # Continue with another password
                elif another_password == 'n':
                    print("Goodbye!")
                    exit()  # Quit the program
                else:
                    print("Please enter 'y' for yes or 'n' for no.")

    except ValueError:
        print("Please enter a valid number.")
