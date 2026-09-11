class Point: # Defining a new data type. (i.e. a new 'Point' class)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('Point\'s moved.', self.x)
    def draw(self):
        print('Point\'s drawn.', self.y)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(self.name, 'is talking.')

point1 = Point(10, 20) # An instance object of the class.
point1.move()
point1.draw()
point2 = Point(1, 2) # Another instance object of the Point class.
point2.draw()
print(point1.x)

person1 = Person('Mohand')
person2 = Person('Ali')
person1.talk()
person2.talk()