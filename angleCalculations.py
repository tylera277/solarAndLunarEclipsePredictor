import math

class AngleCalculations:

    def __init__(self, x_comp,y_comp,z_comp):

        self.x_comp = x_comp
        self.y_comp = y_comp
        self.z_comp = z_comp

    def theta(self, x_comp, y_comp):
        return math.atan(y_comp/x_comp)

    def phi(self,x_comp, y_comp, z_comp):
        return math.atan((math.sqrt(x_comp ** 2.0 + y_comp ** 2.0)) / z_comp)


