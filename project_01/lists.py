names = ['hi', 'there']
print(names[:]) # Reads as names[0:len(names) "i.e. 2"], returning a copy of the whole list.
names[0] = names[0].replace('i', 'iii')
print(names)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print(maximum)

two_dimensional_list = [
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9]
]
for row in two_dimensional_list:
    row_string = ''
    for number in row:
        row_string += str(number) + ' '
    print(row_string)
print('A 3x3 matrix. (2D)')
print(f'First item is {two_dimensional_list[0][0]}.')

# two_dimensional_list.insert(6, 13)
# two_dimensional_list.insert(4, 13)
print(two_dimensional_list)
two_dimensional_list.sort()
two_dimensional_list.reverse()
print(two_dimensional_list)