month = int(input())
match month:
    case 1 | 3 | 5 | 7 | 8 | 10:
        print('31 days.')
    case 4 | 6 | 9 | 11 | 12:
        print('30 days.')
    case 2:
        print('28 days.')
    case _:
        print('Invalid month number.')

# Switch-statement alternative in Python --> match statement.