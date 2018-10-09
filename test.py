import numpy as np
import unittest

from potential import *


class TestElectricFields(unittest.TestCase):

    def test_part_1(self):
        print("**********Testing part 1***************")
        image_array = load_image()
        self.assertTrue(isinstance(image_array, np.ndarray))