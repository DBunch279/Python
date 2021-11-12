# Python OOP Ninja Pets
class Ninja:
    first_name = ""
    last_name = ""
    treats = 0
    pet_food = 0
    pet = None
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet_food = self.pet_food - 1
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

class Pet():
    name = ""
    type = ""
    tricks = []
    health = 50
    energy = 10
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
    
    def sleep(self):
        self.energy = self.energy + 25

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10

    def play(self):
        self.health = self.health + 5
    
    def noise(self):
        if(self.type == "Dog"):
            print("Bark : " + str(self.name) + " Health is " + str(self.health) + " " + str(self.name) + " Energy is " + str(self.energy))
        if(self.type == "Cat"):
            print("Meow : " + str(self.name) + " Health is " + str(self.health) + " " + str(self.name) + " Energy is " + str(self.energy))

class Trained_Pet(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    
    def do_tricks(self):
        for i in range(0, len(self.tricks)):
            print(str(self.name) + " Has Done Trick : " + self.tricks[i])