from util.utils import remove_duplicates

lst = [4, 3, 4, 23, 45, 534, 2, 43546, 5, 3, 4]
print('The list sorted with no duplicates:', sorted(remove_duplicates(lst)))

t = (1, 2, 3)
x, y, z = t # Unpacking a tuple.
print(y)