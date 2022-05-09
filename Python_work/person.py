# # Making People !

# class Person():  # class -> capital   # <- setter 
#     def __init__(self, name, age, height): # <- setter 
#         self.name = name
#         self.height = height
#         self.age = age

#     def talk(self):
#         print(
#             f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.height} tall!")


# will = Person("Will", 31, "6'0''")

# print(will.name) # <- getter
# print(will.age)
# print(will.height)
# will.talk()  # <- getter


# class Car():
#     def __init__(self, top_speed, weight, engine_format):
#         self.top_speed = top_speed
#         self.weight = weight
#         self.engine_format = engine_format

#     def accelerate(self):
#         print(f"We are accelerating up to {self.top_speed}!")

#     def engine_check(self):
#         print(f"I can see that this engine is a {self.engine_format}.")


# Geoffreys_Car = Car(230, "1.8 tons", "V8")

# Geoffreys_Car.accelerate()
# Geoffreys_Car.engine_check()

class Pizza():
    def __init__(self, sauce, topping, crust):
        self.sauce = sauce
        self.topping = topping
        self.crust = crust
    def pizza(self):
        print(f"You have ordered a pizza with a {self.sauce} bace and {self.topping} topping with a {self.crust} crust.")

order1 = Pizza("tomato", "mushroom", "cheese") 
order2 = Pizza("BBQ", "sweetcorn", "thin") 

def orders():
    order1.pizza() 
    order2.pizza()

orders() 