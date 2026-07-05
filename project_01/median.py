l = sorted(eval(input("Please enter a list of numbers: ")))
n = len(l)

try:
    if n % 2 == 1:
        print("The list has an odd number of elements. The median is:", l[n//2])
    else:
        print("The list has an even number of elements. The approximate median is", (l[n//2-1]+l[n//2])/2)
except (IndexError, ValueError):
    print("Please enter a valid list of numbers.")

i, sum = 0, 0
while i < n:
    sum += l[i]
    i += 1
print("Sum of elements in the list is",sum,"\n")

l = sorted(eval(input("Please enter a list of numbers: ")))
myList, myList2 = [], [0]
i = 0
while i < len(l):
    myList += [l[i]*2]
    i += 1

myList2 *= len(myList)
while i > 0:
    i -= 1
    myList2[i] = myList[i] // 2

print("The multiplied version of the list is:",myList,"\n",myList2)