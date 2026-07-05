def capacity(h, l, w):
    return (h*l*w) / 10

h = eval(input("Enter the room's height: "))
l = eval(input("Enter the room's length: "))
w = eval(input("Enter the room's width: "))
capacity = capacity(h, l, w)

print("To cool down your room in 10 minutes or less,", "the capacity should be at least", capacity, "cubic meters per minute.")

l = eval(input("Enter the garden's length: "))
w = eval(input("Enter the garden's width: "))
print("The area of the garden is", str(l*w),"m^2.")
print((l*w)//0.005,"trees could be planted in this area.")