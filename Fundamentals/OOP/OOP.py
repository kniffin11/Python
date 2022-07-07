from operator import truediv


class Dog: 
    # init funciton initializes the parameters. parameters are not attributes, ie. use spike.name not spike.dog_name
    # default parameter goes at the end of hte parameters 
    def __init__(self, dog_name, breed, p_type, age, happpiness = "always wagging my tail"):
        # happiness is a default parameter
        self.name = dog_name
        self.breed = 'golden retriever'
        self.age = 4
        self.personality_type = 'mellow'

class Dog_Example_2: 
    # this applies to all objects
    surname = "supersnoots"
    all_dog_names = []
    # init funciton initializes the parameters. parameters are not attributes, ie. use spike.name not spike.dog_name
    # default parameter goes at the end of hte parameters 
    def __init__(self, data):
        # happiness is a default parameter
        self.name = data["name"]
        self.breef = data["breed"]
        self.age = data["age"]
        self.personality_type = data["p_type"]
        self.energy_level = data["energy_level"]
        # this stores all the instances of name in every object 
        Dog_Example_2.all_dog_names.append(data["name"])
    # keep the class method only 1 indent into the class - it shows that its not an instance method
    @classmethod
    # cls refers to everything within the class, its not self because you use this to pull from eveything 
    def get_all_names(cls): 
        for dog in cls.all_dog_names: 
            print(f"{dog.name}")
    
    @staticmethod
    def check_energy(energy):
        if energy <= 25:
            print("Sorry the dog is to tired")
            return False
        else: 
            return True

    # instance methods you have to pass self as a parameter
    def go_for_a_walk(self):
        # everytime you take him for a walk teh energy level for the object decreases
        self.energy_level = self.energy_level - 5
        print(f"My name is {self.name} owner took me for a stroll and now my energy level is {self.energy_level}")
        return self

    def take_a_nap(self):
        self.energy_level = 100
        print("Zzzzzzzzzzz")
        return self.energy_level

    def eat_a_snack(self):
        if(self.energy_level >= 100):
            print("Im too full")
        else:
            self.energy_level += 5
            print("yum")

spike_data = {
    "name" : "spike",
    "breed" : "Golden Doodle",
    "age" : 5,
    "p_type" : "mellow",
    "energy_level" : 100
}
spike_2 = Dog_Example_2(spike_data)

fido_data = {
    "name" : "Fido",
    "breed" : "Golden Doodle",
    "age" : 5,
    "p_type" : "mellow",
    "energy_level" : 100
}
fido = Dog_Example_2(fido_data)

spike = Dog("Spike", "golden", "mellow", 5)
# brutus = Dog()

print(f"{spike.name} is a {spike.breed} and is {spike.age} years old")

spike_2.go_for_a_walk()
spike_2.go_for_a_walk()
spike_2.go_for_a_walk()
spike_2.go_for_a_walk()
fido.go_for_a_walk()

spike_2.take_a_nap()


