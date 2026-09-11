currList = eval(input("Enter a list: "))
len, i = len(currList), 1
revList = [0] * len

while i <= len:
    revList[len-i] = currList[i-1]
    i += 1

print(revList)