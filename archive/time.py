def reverse1(x):
    rev = 0
    while(x != 0):
        rev *= 10
        rev += x % 10
        x //= 10
    return rev

def reverse2(x):
    rev = ""
    while x != 0:
        rev += str(x%10)
        x //= 10
    return int(rev)

secs = eval(input("Please enter the amount of second you want to calculate: "))
hrs = secs // 3600
secs %= 3600
mins = secs // 60
secs %= 60

print(hrs, "hour," if hrs == 1 else "hours,", mins, "minute," if mins == 1 else "minutes", "and", secs, "second." if secs == 1 else "seconds.")

try:
    print(reverse1(eval(input("Enter a number to reverse: "))))
except ValueError:
    print("Please enter a valid number of digits.")