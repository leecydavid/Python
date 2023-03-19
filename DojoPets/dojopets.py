
class Pet():
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks 
        self.health = 500
        self.energy = 100
        self.noise = noise
    
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f'{self.name} is sleeping. Her energy level is {self.energy}' )
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def sound(self):
        print(self.noise)

class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats 
        self.pet_food = pet_food
        self.pet = pet
    
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        # self.pet = 'walks the Ninja's pet' 
        # .play = invoking the Pet's play() method
        print(f'{self.first_name} is walking {self.pet.name}.')
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        # self.pet = feeds the Ninja's pet 
        # .eat = invoking the Pet's eat() method 
        print(f'{self.first_name} is feeding {self.pet.name} her favorite food -- {self.pet_food}.')
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.sound()
        # self.pet = cleans the Ninja's pet 
        # .noise = invoking the Pet's noise() method
        return self

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.

Ella = Pet('Ella', 'Shiba', 'Tackle Attack', 'WOOF! WOOF! imma smack you if you get my fur wet!')
David = Ninja('David', 'Lee','Peanut Butter', 'liver', Ella)

David.feed().walk().bathe()









