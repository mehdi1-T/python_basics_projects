weight =  float(input("Enter your weight : "))
unit = input("Killograms or Pounds? (L or K) : ").lower()
 
if unit == "p":
    weight = weight / 2.205
    unit = "Kgs "
    print(f"your weight is : {round(weight, 2)} {unit}")

elif unit == 'k':
    weight = weight * 2.205
    unit = 'Lbs'
    print(f"your weight is : {round(weight, 2)} {unit}")

else:
    print(f"{unit} was not valide")

