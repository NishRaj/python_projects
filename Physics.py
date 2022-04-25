from decimal import DivisionByZero


class Physics:
    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass < 0.0 or acceleration < 0.0:
            return 0.0
        return mass*acceleration
    @staticmethod
    def calculate_acceleration(mass, net_force):
        if mass < 0.0 or net_force < 0.0:
            return 0.0
        elif mass == 0.0:
            raise DivisionByZero("Mass cannot be 0.0.")
        return net_force/mass
    @staticmethod
    def calulate_mass(net_force, acceleration):
        if net_force < 0.0 or acceleration < 0.0:
            return 0.0
        elif acceleration ==0.0:
            raise DivisionByZero("Acceleration cannot be 0.")
        return net_force/acceleration