while True:
    try:
        currency = input("Enter the currency used (e.g. EGP, USD, etc.): ").upper()
        balance = float(input("Enter the initial investment amount: "))
        target = float(input("Enter the target amount: "))
        interest = float(input("Enter interest rate (0 to 100): ")) / 100
        break
    except ValueError:
        print("Invalid input. Please retry and enter only valid numbers.")
        continue

if balance >= target:
    print("Your balance already reached your target.")
else:
    years = 0
    while (balance < target):
        years += 1
        balance += (balance * interest)
        print(f'Balance at year {years} is {balance}', currency)
    print("You need",years,"year" if years == 1 else "years","to reach",f"{balance} "+currency,"with","an" if interest >= 0.11 and interest < 0.12 else "a",str(interest*100)+"% annual interest rate.")
    