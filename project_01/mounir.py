name_of_singer = input("Enter the name of the singer: ")

if name_of_singer.lower() in ["mohamed mounir", "mounir"]:
    print("I'm going home.")
else:
    print("I am staying after hours!")

number = eval(input("\nEnter a number: "))
print("The absolute value of",number,"is",str(abs(number))+".")

list = eval(input("Enter a list of values below:\n"))
try:
    print("\nThe 3rd index in your list is",str(list[3])+".\nThe last element is",str(list[len(list)-1])+".\nThe list is of length",str(len(list))+".")
except IndexError:
    print("Invalid length. The list should be 4-element long at least.")

def abs(x):
    return x if (x >= 0) else -x