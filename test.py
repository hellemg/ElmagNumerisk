import numpy as np
import pandas as pd
import unittest

from potential import *
from image import *
from field import *
import plots as pl

from scipy import interpolate
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

class TestElectricFields(unittest.TestCase):

    def test_Image(self):
        print("**********Testing Image***************")
        test_image = Image()
        self.assertTrue(isinstance(test_image.image_array, np.ndarray))

    def test_potential(self):
        print("**********Testing Potential***************")
        def V0_choices(choice):
            return {
                'a': lambda x : np.sin(3 * np.pi * x),
                'b': lambda x : 1 - (x - 1 / 2) ** 4,
                'c': lambda x : np.heaviside(x - 1 / 2, 1) * np.heaviside(3 / 4 - x, 1),
                'd': lambda x : np.ones_like(x) * 20
            }.get(choice, 1)  # 1 is default if x not found

        new_image = Image()
        new_image.extract_coordinates()
        V0 = new_image.interpolate_coordinates()
        self.assertTrue(isinstance(V0, interp1d))

        V = Potential(V0)
        x = V.x_array.copy()
        y = V.V0.copy()
        #pl.plot_array(V.x_array, V.V0)

        V.make_two_dim()
        V.total_potential(100, True)
        X = V.x_array.copy()
        Y = V.y_array.copy()
        Z = V.z.copy()

        E = ElectricField(V)
        Ez_x = E.z_x.copy()
        Ez_y = E.z_y.copy()

        pl.plot_f_V_E(x, y, X, Y, Z, Ez_x, Ez_y)
        #pl.contour_plot_simple(V.x_array, V.y_array, V.z)
        #pl.plot_electricField_simple(E.x_array, E.y_array, E.z_x, E.z_y)

    def test_field(self):
        V = Potential(lambda x: np.sin(3 * np.pi * x))
        V.make_two_dim()
        V.total_potential(100, True)
        E = ElectricField(V)
        #pl.plot_electricField_simple(E.x_array, E.y_array, E.z_x, E.z_y)
