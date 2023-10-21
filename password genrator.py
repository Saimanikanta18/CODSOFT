import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    # Define character sets
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # Generate the password
    Password: str = ''.join(random.choice(characters) for _ in range(length))
    return Password

# Example usage:
password = generate_password(length=16, include_digits=True, include_special_chars=True)
print(password)

