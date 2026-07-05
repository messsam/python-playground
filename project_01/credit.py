def down_payment(is_good, amount):
    if is_good:
        return amount*0.1
    else:
        return amount*0.2

amount = float(input('Enter your amount: '))
print(f'They need to put ${down_payment(False, amount)} down')

i = 0
while i <= 10:
    print('*' * i)
    i += 1
while i >= 0:
    print('*' * i)
    i -= 1