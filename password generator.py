import random
import string

def generate_password(length):
    # Define characters to use for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choices for Python 3.6 and above
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Generate password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
