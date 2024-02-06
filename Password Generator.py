import re # Regular expression operations
import secrets
import string

# default password length is 16 with at least 1 number, special character, uppercase and lowercase letter
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # continue generating a password until all constraints are met
    while True:
        password = ''
        # Generate  a randomized password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'), # all digits 0-9
            (special_chars, fr'[{symbols}]'), # all special characters including underscore
            (uppercase, r'[A-Z]'), # all uppercase letters
            (lowercase, r'[a-z]') # all lowercase letters
        ]

        # Check constraints
        # Make sure there is at least one of each constraint before returning the password        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)