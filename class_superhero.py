class Superhero:
    def __init__(self, hero_name, powers, power_level):
        self.hero_name= hero_name
        self.powers= powers
        self.power_level= power_level
        self.is_hero =True #encapsulated attribute

    def introduce(self):
        print(f"I'am {self.hero_name}, power level {self.power_level}.")

    def use_power(self):
        print(f"Weilding {self.powers},  a power from the heavens")

    #encapsulation (getter method)
    def get_power_level(self):
        return self.power_level
    #encapsulation (setter method)
    def set_power_level(self, new_level):
        if new_level > 0: 
            self.power_level= new_level
            print(f"Power level updated to {new_level}")
        else:
            print("power level must be positive") 
#child class -inherits from Superhero
class anti_hero(Superhero):
    def __init__(self, hero_name, powers, power_level, max_speed):
        super().__init__(hero_name, powers, power_level,)
        self.max_speed=max_speed
    #overriding the use_power method
    def use_power(self):
        print(f"{self.hero_name} flys through the sky at {self.max_speed} mph ")
    def description(self):
        print(f"I {self.hero_name} heavens submits to me at noon")

class overload(Superhero):
    def __init__(self, hero_name, powers, power_level,weapon):
        super().__init__(hero_name, powers, power_level,)
        self.weapon=weapon
    
    #overriding use_power method
    def use_power(self):
        print(f"{self.hero_name} throws his {self.weapon}")
    
    #new method
    def call_weapon(self):
        print(f"{self.weapon} has returned")

#using the classes
print("=========Superheroes presentation=========")

escarnor= anti_hero('escanor', 'Sunshine', 9999999,9999999)
kratos=overload('kratos','rage', 999999,'Blades of chaos')
        
escarnor.introduce() #inherited from Superhero
kratos.introduce()   #inherited from Superhero
escarnor.set_power_level(10000000) #setter method
kratos.set_power_level(1000000) #setter method
escarnor.get_power_level() #getter method
kratos.get_power_level() #getter method
escarnor.use_power() #only anti_hero
escarnor.description() #only anti_hero
kratos.use_power()  #only overload
kratos.call_weapon() #only overload



class Animal:
    def __init__(self,habitat, name, age):
        self.habitat= habitat
        self.name= name
        self.age= age
    def move(self):
        print(f"{self.name} is moving")
    def speak(self):
        print(f"{self.name} is making a sound")

class Dog(Animal):
    def __init__(self, habitat, name, age, breed):
        super().__init__(habitat, name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")
    def move(self):
        print(f"{self.name} runs on all fours")

class Bird(Animal):
    def __init__(self, habitat, name, age, wing_span):
        super().__init__(habitat, name, age)
        self.wing_span = wing_span

    def speak(self):
        print(f"{self.name} chirps")
    def move(self):
        print(f"{self.name} flies with a wingspan of {self.wing_span} meters")

class Fish(Animal):
    def __init__(self, habitat, name, age, fin_count):
        super().__init__(habitat, name, age)
        self.fin_count = fin_count

    def speak(self):
        print(f"{self.name} bubbles")
    def move(self):
        print(f"{self.name} swims with {self.fin_count} fins")

class Lion(Animal):
    def __init__(self, habitat, name, age, pride_size):
        super().__init__(habitat, name, age)
        self.pride_size = pride_size

        def speak(self):
            print(f"{self.name} roars")
        def move(self):
            print(f"{self.name} prowls with a pride of {self.pride_size}")
    
    #demonstrating polymorphism
def animal_parade(animals):
        for animal in animals:
            animal.move()
            animal.speak()
            print(f"{animal.name} lives in {animal.habitat} and is {animal.age} years old.\n")
    
    #creating different animals
animals = [
        Dog("Domestic", "Buddy", 5, "Golden Retriever"),
        Bird("Forest", "Tweety", 2, 0.5),
        Fish("Ocean", "Nemo", 1, 2),
        Lion("Savannah", "Simba", 4, 10)
    ]

animal_parade(animals)  #shows polymorphism in action
