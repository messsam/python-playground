try:
    age = int(input('Age: '))
    income = float(input('Income: '))
    risk = income / age
    print('Risk is', risk) # ValueError with exit code 1 (not 0; i.e. interrupted program flow)
except ValueError:
    print('Please enter a valid numerical value!') # exit code 0
except ZeroDivisionError:
    print('Age cannot be zero!') # exit code 0