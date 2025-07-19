 
class car: 
    #constructor
    def __init__(self,color,engine):
        self.color = color
        self.engine = engine

# class function(methods)
def start(self):
    print("vroom vroom")

def stop(self):
    print("car is stopped")

def details (self):
    print(f"the car color is {self.color} and the engine type is {self.engine}")


# creating objects 
bmwobj = car("blue","petrol") #bmw object has been created from car class
bmwobj.start()    
bmwobj.stop()    
bmwobj.sdetails()    
        