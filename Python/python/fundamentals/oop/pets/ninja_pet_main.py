# Python OOP Ninja Pets
from ninja_pet import Ninja, Pet, Trained_Pet

def main():
    craig = Ninja("Craig", "Thomas", 10, 10, Pet("Pooch", "Dog", []))
    craig.feed()
    craig.bathe()
    craig.walk()

    allie = Ninja("Allie", "Camrod", 5, 7, Pet("Roxy", "Cat", []))
    allie.feed()
    allie.walk()
    allie.bathe()
    allie.pet.sleep()

    john = Ninja("John", "Sage", 10, 2, Trained_Pet("Park", "Dog", ["Fetch", "Chase Cats and Other Dogs", "Run Laps", "Do Three Back Flips"]))
    john.feed()
    john.pet.sleep()
    john.bathe()
    john.walk()
    print("")
    john.pet.do_tricks()

if(__name__ == "__main__"):
    main()