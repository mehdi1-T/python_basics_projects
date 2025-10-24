user_name = input("enter your full name : ")


first_name = user_name[:user_name.index(" ")]
last_name = user_name[user_name.index(" "):]

print('your first name : ', first_name)
print('your last name : ', last_name)