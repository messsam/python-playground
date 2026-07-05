# Experimental Python refresher.

import math

# Driver main function to invoke and test functions.

def main():
    print(f(4, 6))
    print(reverse("Hello world!"))
    print(encoding("Hello world!"))
    print(palindrome("Jack"))
    print(palindrome("JaccaJ"))
    x, y = eval(input("Enter value x: ")), eval(input("Enter value y: "))

    print("GCD of "+str(x)+" and "+str(y)+" is "+str(gcd(x, y)))
    print("Factorial of "+str(x)+" is "+str(factorial1(x)))
    print("Sum of numbers up to "+str(y)+" is "+str(sumUpTo(y)))

    float = 23.2
    print(float)
    float = input("Please enter your name: ")
    print("Hello,",float+"!")
    print(x+1)

    print(math.sqrt(16))
    print(digitSum(32))

# Function definitions. (i.e. program core)

def reverse(string):
    reverse = ""
    i = len(string)-1
    while i >= 0:
        reverse += string[i]
        i -= 1
    return reverse

def palindrome(string):
    return string == reverse(string)

def occurrences(string, char):
    occurrences, i = 0, 0
    while i < len(string):
        if string[i] == char:
            occurrences += 1
        i += 1
    return occurrences

def occurs(string, char):
    return occurrences(string, char) > 0

def encoding(string):
    output, i = "", 0
    while i < len(string):
        curr = string[i]
        if curr.isalpha() and not occurs(output, curr):
            output += str(occurrences(string, curr)) + curr
        i += 1
    return output

def gcd(x, y): 
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def factorial1(n):
    if (n == 0):
        return 1
    else:
        return n * factorial1(n-1)

def factorial2(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

def sumUpTo(n):
    total = 0
    while n != 0:
        total += n
        n -= 1
    return total

def digitSum(x):
    sum = 0
    while x != 0:
        sum += x % 10
        x //= 10
    return sum

def largest():
    largest = -math.inf
    while True:
        input_value = input("Enter a number (or 'exit' to print the result): ")
        if (input_value.lower() == "exit"):
            break
        try:
            input_value = float(input_value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if (input_value > largest):
            largest = input_value
    return largest

def f(x, y):
    return math.sqrt(sq(x) + sq(y))

def sq(x):
    return x*x

# Portal to the module's main function.

if __name__ == "__main__":
    main()