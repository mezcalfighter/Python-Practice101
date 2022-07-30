class Dog():

    # Class Object Attribute
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed="Lab",name="Ema")
print("Breed:",mydog.breed,"Name:",mydog.name)

otherdog = Dog("Husky","Carlos")
print("Breed:",otherdog.breed,"Name:",otherdog.name,"Species:",otherdog.species)