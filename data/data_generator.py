from random import randint, choice

ALLOWED_PREFIXES = ('+2010', '+2011', '+2012', '+2015')
LETTERS ='abcdefghijklmnopqrstuvwxyz'

def generate_user_data(count=10000):
	"""Generates a dictionary pairing unique phone numbers to random usernames."""
	registry = {}

	for _ in range(count):
		number = choice(ALLOWED_PREFIXES) + ''.join(str(randint(0, 9)) for _ in range(8))
		user = choice(LETTERS).upper() + ''.join(choice(LETTERS) for _ in range(randint(2, 9)))

		registry[number] = user

	return registry