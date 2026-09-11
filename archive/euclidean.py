x1, y1 = eval(input("Enter 1st  point's x: ")), eval(input("Enter 1st point's y: "))
x2, y2 = eval(input("Enter 2nd point's x: ")), eval(input("Enter 2nd point's y: "))

import math
print("The distance between the points is: " + str(math.sqrt((x2-x1)**2 + (y2-y1)**2)))

nbr_of_eggs = eval(input("Enter the number of eggs you have: "))
dozens = nbr_of_eggs // 12
remaining = nbr_of_eggs % 12
print("You have",dozens,"dozens and",remaining,"remaining","egg" if remaining == 1 else "eggs")

radius = eval(input("Enter the radius: "))
while (True):
    response = input("Type A for area or C for circumference: ")
    if (response.lower() == "a"):
        area = (radius * radius * 3.14)
        print("Area is",area)
        break
    elif (response.lower() == "c"):
        circumference = (2 * radius * 3.14)
        print("Circumference is",circumference)
        break
    else:
        print("Invalid input. valid inputs are: \"A/a\" or \"C/c\". Please retry again.")
        continue