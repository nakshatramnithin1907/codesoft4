import string
import random
def generate_password(length):
    if length < 6: 
        print("Password length should be at least 6 characters.")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation  
    password = ''.join(random.choice(characters) for i in range(length))
    return password
desired_length = int(input("Enter the desired length of the password: "))

password = generate_password(desired_length)
if password:
    print("Your generated password is:", password)
1