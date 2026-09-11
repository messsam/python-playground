from abc import ABC, abstractmethod

class Animal (ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_moving = False

    def move(self):
        if not self.is_moving:
            self.is_moving = True
            print(self.name, 'started moving.')
        else:
            print(self.name, 'is already moving.')

    def stop(self):
        if self.is_moving:
            self.is_moving = False
            print(self.name, 'stopped.')
        else:
            print(self.name, 'is already not moving.')

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Meow Meow')


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Hrr Hrr')

if __name__ == '__main__':
    dog = Dog('Mike', 3)
    cat = Cat('Lili', 10)
    dog.make_sound()
    dog.stop()
    cat.move()