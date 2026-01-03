class Dog:
    def sounds(self):
        print("Dog barks")
        
class Cat:
    def sounds(self):
        print("Cat meows")
        
animals = ((Dog(), Cat()))

for i in animals:
    i.sounds()