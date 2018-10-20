import sys
print("Python: " + sys.version, end='\n\n')

class car:

    name = ""
    maxSpeed = 0
    mileage = 30 #in km/Lt.
    currentSpeed = 0
    timeDriven = 0

    def __init__(self, car_name, max_speed):
        self.maxSpeed= max_speed
        self.name = car_name

    def set_speed(self):
        while self.currentSpeed == 0:
            x = int(input("Input the current speed for " + self.name + ": "))
            if (x > self.maxSpeed):
                print("Enter a valid speed.")
            else:
                self.currentSpeed = x

    def drive(self):
        #nonlocal mileage
        self.mileage = self.mileage - int(input("Please input the number of hours driven for " + self.name + ": "))

    def show_status(self):
        print("Current Speed for " + self.name + ": ",self.currentSpeed, " km/Lt.")
        print("Mileage for " + self.name + ": ", self.mileage, " km/Lt.")

a = car("Golf", 180)
b = car("Polo", 150)

a.set_speed()
b.set_speed()

a.drive()
b.drive()

a.show_status()
b.show_status()

class convertible(car):

    roofUpTime = 0

    def __init__(self, car_name, max_speed, roof_time):
        car.__init__(self, car_name, max_speed)
        self.roofUpTime = roof_time

    def show_status(self):
        print("Current Speed for " + self.name + ": ", self.currentSpeed, " km/Lt.")
        print("Mileage for " + self.name + ": ", self.mileage, " km/Lt.")
        print("Roof up time for " + self.name + ": ", self.roofUpTime, " seconds.")

c = convertible("Mazda CX 5", 200, 30)

c.set_speed()

c.drive()

c.show_status()
