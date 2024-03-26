
class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors += floors
        print('NumberOfFloors: ', self.numberOfFloors)

house = House()
house.setNewNumberOfFloors(floors=5)