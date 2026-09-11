def grades_mapping(grade):
    if grade < 0:
        return 'Invalid mark; less than 0.'
    elif grade > 105:
        return 'Invalid mark; greater than 105.'
    elif grade < 50:
        return 'F'
    elif grade < 60:
        return 'D'
    elif grade < 74:
        return 'C'
    elif grade < 85:
        return 'B'
    else:
        return 'A'


grade = float(input('Grade: '))
print(grades_mapping(grade))