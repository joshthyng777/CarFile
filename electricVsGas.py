class Car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
        self.currentMiles = 0
    
    def carInfo(self):
        print(f"{self.year} {self.name} with a {self.color} finish.") #Prints out the information about the car.
    
    def readMileage(self):
        print(f"This car has {self.currentMiles} miles\n") #Prints the miles of the car, default mileage is set to 0.
    
    def updateMiles(self, addMiles):
        self.currentMiles += addMiles #Function allows you to add mileage.

#Creating our battery class
class Battery():
    def __init__(self, battery_size=80):
        self.battery_size = battery_size
        
    def batteryInfo(self):
        print(f"This car has a battery size of {self.battery_size} KwH")

#Creating our electric car class that inharites for the parent class Car.
class ElectricCar(Car): 
    def __init__(self, name, year, color):
        super().__init__(name, year, color) #Super gives us access to the parent functions
        self.battery = Battery()
        
    def getRange(self):
        if self.battery.battery_size <= 80: #Note that each instance of battery are called with .battery.battery_size (The function name and the piece we are calling)
            print(f"On a full charge of {self.battery.battery_size} the {self.name.title()} can go 125 miles!")
        elif self.battery.battery_size > 80:
            print(f"On a full charge of {self.battery.battery_size}KwH the {self.name.title()} can go 250 miles!")
    
    def updateBattery(self, numUpdate):
        self.battery.battery_size += numUpdate
        
elec = ElectricCar('tesla', 2021, 'black') #Creates the electric car from the child class "ElectricCar"
elec.updateBattery(101) #Adds 100 to the original 80 battery.
elec.carInfo()
elec.battery.batteryInfo()
elec.getRange() 

print("\nGas vehicle information:")
##
car1 = Car('land rover', 2024, 'white')
car1.carInfo()
car1.updateMiles(1002)
car1.readMileage()