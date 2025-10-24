its_raining = input("is it raining (yes/no) : ").lower()
its_cold = input("is it cold (yes/no) : ").lower()
homework = input("do you have homeworks : ").lower()


if homework == 'yes':
    print("funish your homework first ")

elif its_raining == 'yes' and its_cold == 'yes':
    print("Stay home and drink hot chocolate.")

elif its_raining == 'yes' and its_cold == 'no':
    print("perfect day for outdoor activities.")

elif its_cold == 'yes' and its_raining == 'no':
    print("Wear a jaket and go outside")

else:
    print("invlide inputs")
