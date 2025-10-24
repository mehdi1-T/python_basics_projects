import math

# print(math.pi)
# print(math.e)
# print(round(math.sqrt(9)))
# print(math.ceil(3.1))#round the number up
# print(math.floor(3.1))#round the number down

def circle_area():
    raduis = float(input("enter the raduis of the circle"))
    area = math.pi *  pow(raduis, 2)
    print(f"the area of the circle is {round(area, 2)}cm")

circle_area()








# x = 3.14
# y = 5
# z = 2

# result = round(x)
# result = abs(y)
# result = pow(y, z)
# res = max(x, y, z)
# res = min(x, y, z)

# print(res)