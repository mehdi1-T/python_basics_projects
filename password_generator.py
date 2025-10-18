import colorama
import random
import string



def generat_password(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return 'your password: '+password

   
   
lenght = int(input("Enter the password lenght: "))
print("Yout password: ", generat_password(lenght))
