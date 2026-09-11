message = input('Enter a message: ')

if len(message) < 10:
    print('The minimum is 10 characters.')
elif len(message) > 50:
    print('The maximum allowed is 50 characters.')
else:
    print('succeeded.')

print('Rest of code..')