print(__file__)
input_num, i, sum = int(input("Enter the amount of numbers required: ")), 0, 0

while (i < input_num):
    sum += float(input("Enter a number: "))
    i += 1

print("The average of the",input_num,"numbers is:",sum/input_num)

x, y = eval(input("Enter x: ")), eval(input("Enter y: "))
multiplication = x
i = 1

while (i < y):
    multiplication += x
    i += 1

print(x,"times",y,"is",multiplication)

from algorithms import factorial2
print("Factorial",x,"is",factorial2(x))

from algorithms import largest
print("Largest number is",largest())