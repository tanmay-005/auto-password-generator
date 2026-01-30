import string
import secrets


def generate_password():
    print("--Auto Password Generator--")


    ## Password Length Input
    Length = int(input("Enter the Length of Password : "))

    if Length <= 0:
        print("Password Length must be greater than 0.")
        return
    
    ## User Input
    use_upper = input("Include uppercase letters? (y/n): ").lower()
    use_lower = input("Include lowercase letters? (y/n): ").lower()
    use_digits = input("Include digits? (y/n): ").lower()
    use_special = input("Include special charaters? (y/n): ").lower()


    characters = ""
    password = ""

    ## Building character set based on user input
    if use_upper =='y':
        characters += string.ascii_uppercase
        password += secrets.choice(string.ascii_uppercase)

    if use_lower == 'y':
        characters += string.ascii_lowercase
        password += secrets.choice(string.ascii_lowercase)
        
    if use_digits == 'y':
        characters += string.digits
        password += secrets.choice(string.digits)

    if use_special == 'y':
        characters += string.punctuation
        password += secrets.choice(string.punctuation)


    ## Validating character set
    if Length < len(password):
        print("Password length is too short.")
        return
    ## Generating remaining characters
    remaining = Length - len(password)
    for _ in range(remaining):
        password += secrets.choice(characters)

    print("\nGenerated password: ", password)

generate_password()