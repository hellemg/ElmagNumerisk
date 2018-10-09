import numpy as np

class ElectricField:
    def __init__(self, potential):
        z = np.gradient(potential.z)
        self.z_x = z[0]*(-1)
        self.z_y = z[1]*(-1)
        self.x_array = potential.x_array
        self.y_array = potential.y_array
