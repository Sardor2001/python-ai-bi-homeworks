# Parent class: Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child class: Cow
class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production  # Liters of milk per day

    def make_sound(self):
        return "Moo!"

    def produce_milk(self):
        print(f"{self.name} produced {self.milk_production} liters of milk.")


# Child class: Sheep
class Sheep(Animal):
    def __init__(self, name, age, wool_length):
        super().__init__(name, age)
        self.wool_length = wool_length  # Length of wool in centimeters

    def make_sound(self):
        return "Baa!"

    def shear_wool(self):
        print(f"{self.name} was sheared. Wool length is now 0 cm.")
        self.wool_length = 0


# Child class: Chicken
class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.eggs_laid = 0  # Number of eggs laid

    def make_sound(self):
        return "Cluck!"

    def lay_egg(self):
        self.eggs_laid += 1
        print(f"{self.name} laid an egg! Total eggs laid: {self.eggs_laid}.")


# Farm simulation
if __name__ == "__main__":
    # Create animals
    cow = Cow("Bessie", 5, 10)
    sheep = Sheep("Woolly", 3, 15)
    chicken = Chicken("Clucky", 2)

    # Simulate behaviors
    print(f"{cow.name} says: {cow.make_sound()}")
    cow.produce_milk()

    print(f"{sheep.name} says: {sheep.make_sound()}")
    sheep.shear_wool()

    print(f"{chicken.name} says: {chicken.make_sound()}")
    chicken.lay_egg()
