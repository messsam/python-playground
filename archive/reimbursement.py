expenses = float(input("Please enter your eligible medical expenses: "))

if (expenses <= 100):
    print("The insurance does not cover the first 100 LE of medical expenses.")
elif (expenses <= 2000):
    print("The reimbursement amount is",(expenses-100)*0.9)
else:
    print("The reimbursement amount is",(1900*0.9)+(expenses-2000))

while (1):
    output = 1
    user_input = input()
    if user_input.lower() == "kefaya":
        break
print(output)