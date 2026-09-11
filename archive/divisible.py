x = eval(input('Enter a number: '))
print('Try again.' if x < 0 else f'{x} is the product of 7*{x//7}.' if x % 7 == 0 else f'{x} is not divisible by 7.')