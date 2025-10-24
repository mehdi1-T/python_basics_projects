age = int(input("How old are you : "))
key = input("Have you the keys (yes/no) : ").lower()
admin = input("Are you an admin (yes/no) : ").lower()

if (age >= 18 and key == 'yes') or (admin == 'yes'):
    print("The door is opned")
else : 
    print("you can't open the door")    
