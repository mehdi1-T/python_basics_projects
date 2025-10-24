unit = input("enter is this temperature in Celsius or Fahrenheit (C/f): ")
temp = float(input("enter this temperature : "))

if unit.lower() == 'c':
    temp =  9 * temp / 5 + 32
    print(f"{temp} °F")
elif unit.lower() == 'f':
    temp = (temp - 32) * 5 / 9 
    print(f"{temp} °C")


else:
    print("invalide unit")