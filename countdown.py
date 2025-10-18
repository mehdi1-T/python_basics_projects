from playsound import playsound
import time

user = int(input("enter a number to countdown starting from it : "))

for i in range(user,0,-1):
    print(i)
    time.sleep(1)

playsound(r"C:\Users\bismiallah\Desktop\python\basics\notification-sound-type-18-no-copyright-410280.mp3")