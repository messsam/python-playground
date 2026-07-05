for item in ['Hello', 'World', '!']: # Like enhanced for loops in Java.
    print(item)

for number in range(10): # Creates an object (that's not a list) containing numbers 0 to 9
    print(number)

for number in range(3, 11): # From 3 to 10
    print(number)

for number in range(3, 12, 2): # 3, 5, 7, 9, 11 (Using 2 as a step factor)
    print(number)

for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [2, 2,2, 2, 5]

for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)