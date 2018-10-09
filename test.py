import numpy as np
import unittest

from potential import *
from image import *
from field import *
import plots as pl

class TestElectricFields(unittest.TestCase):

    def test_part_1(self):
        print("**********Testing part 1***************")
        test_image = Image()
        self.assertTrue(isinstance(test_image.image_array, np.ndarray))

    def test_potential(self):
        V = Potential(lambda x : np.sin(3 * np.pi * x))
        #print("Potential: ", V.func)
        #pl.plot_array(V.x_array, V.func)
        #V.set_y(V.y_array+0.5)
        V.make_two_dim()
        V.total_potential(100, True)
        #pl.contour_plot_simple(V.x_array, V.y_array, V.z)

    def test_field(self):
        V = Potential(lambda x: np.sin(3 * np.pi * x))
        # print("Potential: ", V.func)
        # pl.plot_array(V.x_array, V.func)
        # V.set_y(V.y_array+0.5)
        V.make_two_dim()
        V.total_potential(100, True)
        #pl.contour_plot_simple(V.x_array, V.y_array, V.z)
        E = ElectricField(V)
        pl.plot_electricField_simple(E.x_array, E.y_array, E.z_x, E.z_y)
