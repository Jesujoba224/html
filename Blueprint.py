"""
class : blueprints
object : instance of class



variable : storage unit for data
instance variable : a variable inside a class but not outside a method


OOPS ?

Was created to make code more reusable and organized 
Revolves around classes and objects
properties of OOPS :
inheritance, polymorphism, encapsulation, abstraction""

"""
class car:
    print("hey! I have 4 wheels and 2 side mirrors and a windshield")
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
        
    def start(self):
        print("I started")
            

lamborghini=car("aventador","yellow","2020")
print(lamborghini.name)
print(lamborghini.color)
print(lamborghini.model)
print(lamborghini.start())