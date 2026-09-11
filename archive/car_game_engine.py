class Car:
    def __init__(self):
        self.is_on = False

    def start(self):
        if not self.is_on:
            self.is_on = True
            print('Car started!')
        else:
            print('Car\'s already on.')

    def stop(self):
        if self.is_on:
            self.is_on = False
            print('Car stopped!')
        else:
            print('Car\'s already off.')

car = Car()

while True:
    command = input('> ').lower()
    if command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == 'start':
        car.start()
    elif command == 'stop':
        car.stop()
    elif command == 'quit':
        exit(0) # Successful exit.
    else:
        print('Invalid input.')