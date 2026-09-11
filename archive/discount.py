amount = float(input('Enter the cost of the purchase: '))
if amount > 1000:
    amount -= amount * 0.05
print(f'The amount to be paid after applicable discounts and taxes is {amount + amount * 0.1} EGP.')

dog_age = int(input('Enter a dog\'s age in dog years: '))
if dog_age < 0:
    print('Age must be a natural number.')
else:
    print('The dog\'s age in human years is', dog_age * 10.5 if dog_age <= 2 else (dog_age - 2) * 4 + 21)