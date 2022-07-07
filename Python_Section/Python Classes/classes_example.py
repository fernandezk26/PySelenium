#classes are what makes OOP, OOP
#classes are a blueprint for an object

class Animal:
    def __init__(self, color, food_type) -> None:
        print("I am init")
        self.color = color
        self. food_type = food_type

    def move(self): 
        print("animal moves")

    def eat(self):
        print("animal eat")
        print("This animal eats {}".format(self.food_type))

    def breathe(self):
        print("Animal breathes")

    def main(self):
        self.eat()
        self.move()

my_animal = Animal('blue', 'Meat')
print(f"color of animal: {my_animal.color}")
print(my_animal.move())

my_animal_2 = Animal('red', 'chicken')
print(my_animal_2.eat())
