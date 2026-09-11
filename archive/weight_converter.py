from util import converters

weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    print(f'You are {converters.lbs_to_kg(weight)} kg.')
elif unit.upper() == 'K':
    print(f'You are {converters.kg_to_lbs(weight)} lbs.')
else:
    print('Invalid unit.')