# create a class car

class Car:

    def __init__():
        print("---   Car   ---")

    def __init__(self, userCarName, userCarSeat, userCarEngine):
        self.carName = userCarName
        self.carSeats = userCarSeat
        self.carEngine = userCarEngine

        print("car name : ", self.carName)
        print("car seating : ", self.carSeats)
        print("car Engine : ", self.carEngine)
    
    def start(self):
        print("car started...")
        print("rrrrrrrr")

    def stop(self):
        print("car stopped")

userCar1 = Car("Maruti-800", 5, 800)
userCar1.start()
userCar1.stop()