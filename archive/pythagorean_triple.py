m, n = eval(input('m: ')), eval(input('n: '))
print('The Pythagorean Triple:')
a = m**2 - n**2
print('a =', a)
b = 2*m*n
print('b =', b)
import math
print(f'c = {math.sqrt(a**2 + b**2)}')