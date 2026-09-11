from data_generator import generate_user_data

registry = generate_user_data(1000000)
print(registry)

def find_user(number, registry):
    return registry.get(number)

search_number = '+201065200682'
user = find_user(search_number, registry)

if user is None:
    print(f"Cannot find a user with the number {search_number}.")
else:
    print(f"User '{user}' was found with number {search_number}.")