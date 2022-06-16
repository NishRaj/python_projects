from abc import ABC, abstractmethod
class Animal(ABC):

    
    @abstractmethod
    def sleep(self):
        print("ZZZZ")
    
    @abstractmethod
    def animal_sound(self):
        #raise NotImplementedError("Please provide implementation of animal_sound() method.")
        pass
    
    def wake_up(self):
        self.animal_sound()
        print("I am awake!")

class Lion(Animal):
    
    def animal_sound(self):
        print("Roar!")
    
    def sleep(self):
        super().sleep()
        print("Lion Sleeping")

lion = Lion()
animal = Animal()
#animal.sleep()
lion.animal_sound()
lion.sleep()