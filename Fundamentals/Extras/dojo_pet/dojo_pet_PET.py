class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100

    def sleep(self):
        if((self.energy + 25) > 100):
            print("He isn't tired")
        else: 
            self.energy += 25
            print(self.energy)

    def eat(self):
        if((self.energy + 5) <= 100):
            self.energy += 5
            print(self.energy)
        else:
            print("He has enough energy!")
        if((self.health + 10) <= 100):
            self.health += 10
            print(self.health)
        else:
            print("He has enough health!")

    def play(self):
        if((self.health + 5) <= 100):
            self.health += 5
            print(self.health)
        else:
            print("He has enough health!")

    def noise(self):
        print("ruff ruff!")

# just to practice inheritence

# need to include the parent class within parenthesis
class Pets(Pet):
    def __init__(self, name, has_siblings):
        # super refers to the parent class
        super.__init__(self, name)
        self.has_siblings = has_siblings