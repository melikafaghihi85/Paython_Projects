class Animal():
    def __init__(self,name,species,age,sound):
       self.name = name
       self.species = species
       self.age = age 
       self.sound = sound
    def  make_sound(self):
        print(f"{self.name} says: {self.sound}")
    zoo_name = 'Zoo'
    def info(self):
        print(f"Zoo: {Animal.zoo_name}")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
    def __str__(self):
        return (f"Animal(Name: {self.name}, "
                f"Species: {self.species}, "
                f"Age: {self.age}, "
                f"Sound: {self.sound})")
class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span 
    def make_sound(self):
        print(f"{self.name} chirps: {self.sound}")
    def info(self):
        super().info()
        print(f"Wing Span: {self.wing_span} cm")

lion = Animal("Lion", "Mammal", 5, "Roar")
print("Animal Information")
lion.info()
lion.make_sound()
print(lion)
print("-" * 40)
bird = Bird("Woodpecker", "Bird", 2, "Drdrdr", 45)

print("Bird Information")
bird.info()
bird.make_sound()
print(bird)