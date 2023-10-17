class OptionalParameters:
    def __init__(self, make, model, year, condition="New", kms=0 ) -> None:
        self.make = make
        self.model = model
        self.year= year
        self.condition = condition
        self.kms = kms
    '''
    Use continuation character / in case of long lines in Python.
    '''
    def display(self, show_all = True):
        if show_all:
            print(f"The make and model of the car is {self.make} {self.model}.It is manufactured in {self.year}. \
It has run {self.kms} and its condition is {self.condition}")
        else:
            print(f"The make and model of the car is {self.make} {self.model}.It is manufactured in {self.year}.")

car = OptionalParameters('Skoda', 'Octavia', '2016', 'old', 35000)
car.display(False)