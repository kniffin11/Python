import dojo_pet_PET

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        self.Pet_class = dojo_pet_PET.Pet('Natalie', 'Dolphin', 'swim')
    
    def walk(self):
        self.Pet_class.play()

    def feed(self):
        self.Pet_class.eat()

    def bathe(self):
        self.Pet_class.noise()

sam = Ninja('sam', 'chance', 'biscuits', 'kibble', 'dog')
sam.walk()
sam.bathe()
sam.walk()
