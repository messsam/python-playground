amount = eval(input("Enter the amount to be converted: "))
type = eval(input("Type of service; enter \"1\" to convert from EUR to EGP, and \"2\" to convert EGP to EUR: "))
exchange = eval(input("Enter the current exchange rate (i.e. 1 EUR price in EGP): "))

if (type == 1):
    print(amount*exchange)
elif (type == 2):
    print(amount/exchange)
else:
    print("Invalid input: please choose 1 or 2 as the type of the service.")