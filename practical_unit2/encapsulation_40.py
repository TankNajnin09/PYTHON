class Car:
    def __init__(self):
        self.__updateSoftware()
        
    def drive(self):
        print("Driving")

    #private method
    def __updateSoftware(self):
        print("updating software is private method")

redcar = Car() 
redcar.drive() 
#redcar.__updateSoftware()  not accesible from object. 
