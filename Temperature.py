class Temperature:
    
    min_temperature = 0
    max_temperature = 1000
    def __init__(self,kelvin):
        self.kelvin = kelvin
        if kelvin < Temperature.min_temperature or kelvin > Temperature.max_temperature:
            raise Exception("Invalid temperature")
    
    @classmethod
    def update_min_temperature(cls,min_temp):
        if min_temp > cls.max_temperature:
            raise Exception("Invalid temperature.")
        cls.update_min_temperature = min_temp
    @classmethod
    def update_max_temperature(cls,max_temp):
        if max_temp < cls.min_temperature:
            raise Exception("Invalid temperature")
        cls.max_temperature = max_temp
t1 = Temperature(260)
Temperature.update_max_temperature(270)
Temperature.update_min_temperature(680)