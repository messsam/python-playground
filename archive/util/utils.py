digits_mapping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}

def digit_to_str(digit):
    return digits_mapping.get(digit, '*')

def number_to_str(number):
    try:
        string = ''
        for digit in number:
            string += digit_to_str(digit) + ' '
        return string
    except IndexError:
        print('Index out of range; the returned value is None.')
        return None

def find_max(lst):
    try:
        maximum = lst[0]
        for element in lst:
            if element > maximum:
                maximum = element
        return maximum
    except IndexError:
        print('Index out of range; the returned value is None.')
        return None

def remove_duplicates(lst):
    try:
        for element in lst:
            while lst.count(element) > 1:
                lst.remove(element)
        return lst
    except IndexError:
        print('Index out of range; the returned value is None.')
        return None