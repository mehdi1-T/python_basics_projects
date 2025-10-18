import random
import string

def generate_password(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password

lenght = int(input("Please, Enter character number: "))
print("your password: ",generate_password(lenght))
