original = eval(input('The price of the item in year 1984 is '))
inflated = eval(input('The price of the item in year 2014 is '))
print(f'The CPI is {((inflated-original)/original)*100}%')