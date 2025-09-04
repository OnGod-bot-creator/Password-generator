import string
import random

# Function to calculate the strength of a password based on its length
def password_strength(password):
    # The strength of the password is currently determined by its length
    strength = len(password)
    return strength
# Function to generate a password based on user input
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True,
                      include_phrase=None):
    # Initialize an empty string to store the characters to choose from
    characters = ''
    # Add uppercase letters to the characters if the user wants to include them
    if use_uppercase:
        characters += string.ascii_uppercase
    # Add lowercase letters to the characters if the user wants to include them
    if use_lowercase:
        characters += string.ascii_lowercase
    # Add digits to the characters if the user wants to include them
    if use_digits:
        characters += string.digits
    # Add symbols to the characters if the user wants to include them
    if use_symbols:
        characters += string.punctuation

    # Initialize the password with the included phrase if there is one
    password = include_phrase if include_phrase else ''

    # Continue adding random characters to the password until it reaches the desired length
    while len(password) < length:
        password += random.choice(characters)
    # Print the generated password
    print(f"\nYour generated password is: {password}")
    # Calculate the strength of the password
    strength = password_strength(password)

    # Print the strength of the password
    print(f"Password strength: {'Weak' if strength < 5 else 'Moderate' if strength < 8 else 'Strong'}")
# Main program loop
while True:
    try:
        # Ask the user for the length of the password
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        # If the user enters something that's not a number, ask again
        print("Invalid input. Please enter a number.")

while True:
    # Ask the user if they want to include uppercase letters
    use_uppercase = input("Include uppercase letters? (y/n): ").lower()
    if use_uppercase in ['y', 'n']:
        # Convert the user's input to a boolean value
        use_uppercase = use_uppercase == 'y'
        break
    else:
        # If the user enters something that's not 'y' or 'n', ask again
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    # Ask the user if they want to include lowercase letters
    use_lowercase = input("Include lowercase letters? (y/n): ").lower()
    if use_lowercase in ['y', 'n']:
        # Convert the user's input to a boolean value
        use_lowercase = use_lowercase == 'y'
        break
    else:
        # If the user enters something that's not 'y' or 'n', ask again
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    # Ask the user if they want to include digits
    use_digits = input("Include digits? (y/n): ").lower()
    if use_digits in ['y', 'n']:
        # Convert the user's input to a boolean value
        use_digits = use_digits == 'y'
        break
    else:
        # If the user enters something that's not 'y' or 'n', ask again
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    # Ask the user if they want to include symbols
    use_symbols = input("Include symbols? (y/n): ").lower()
    if use_symbols in ['y', 'n']:
        # Convert the user's input to a boolean value
        use_symbols = use_symbols == 'y'
        break
    else:
        # If the user enters something that's not 'y' or 'n', ask again
        print("Invalid input. Please enter 'y' or 'n'.")

while True:
    # Ask the user if they want to include a phrase
    include_phrase = input("Include a phrase? (y/n): ").lower()
    if include_phrase in ['y', 'n']:
        # Convert the user's input to a boolean value
        include_phrase = include_phrase == 'y'
        if include_phrase:
            # If the user wants to include a phrase, ask them to enter it
            include_phrase = input("Enter the phrase: ")
        break
    else:
        # If the user enters something that's not 'y' or 'n', ask again
        print("Invalid input. Please enter 'y' or 'n'.")
# Generate the password based on the user's input
generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols, include_phrase)