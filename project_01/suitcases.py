# Consider an airport boarding counter. Each passenger carries two suitcases with no extra
# charge if the weight is 23 Kg, or less, per each. The passenger will have to pay an extra
# charge of 50 LE per extra Kg for extra weight, up to a maximum weight of 32Kg per suitcase.
# If a suitcase weight exceeds 32Kg, the suitcase is rejected. Write a Python program that
# takes as input weights of two suitcases and prints out the weight charge.

try:
    sc1_weight = float(input('First suitcase\'s weight: '))
    sc2_weight = float(input('Second suitcase\'s weight: '))

    sc1_charge = (sc1_weight - 23) * 50 if 23 < sc1_weight <= 32 else 0
    sc2_charge = (sc2_weight - 23) * 50 if 23 < sc2_weight <= 32 else 0

    print('Suitcase 1', 'accepted' if 0 <= sc1_weight <= 32 else 'rejected')
    print('Suitcase 2', 'accepted' if 0 <= sc2_weight <= 32 else 'rejected')
    print('Total charge =', sc1_charge + sc2_charge,'EGP')
except ValueError:
    print('Invalid-value error. Please enter valid numerical weights.')