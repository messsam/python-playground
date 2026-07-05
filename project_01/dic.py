from util.utils import digit_to_str, number_to_str

customer = {
    'name': 'Mohand',
    'age': 17,
    'number': '+20116658995',
    'email': 'mo@gmail.com',
    'is_verified': True
    # Keys should be unique. (And obviously values can be duplicated 3ady)
}

print(customer['name'])
customer['name'] = 'John Smith'
print(customer.get('name', 'Unknown'))

# Dynamically adding key-value pairs:
customer['birthdate'] = 'Feb 2, 2006'
print(customer.get('birthdate'))
print(customer)

number = input('Enter a number: ')
print(digit_to_str(number[0]))
print(number_to_str(number))