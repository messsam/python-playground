weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

BMI = weight / (height/100)**2

print('Underweight' if BMI <= 18.5 else 'Fit' if BMI <= 25 else 'Overweight')

capacity = float(input('Tank capacity: '))
percent = float(input('Gas Gauge Reading in percent: '))
miles = float(input('Miles per Gallon: '))

distance = capacity * (percent/100) * miles

print('Get gas!' if distance < 200 else 'It\'s okay. I forgive you.')