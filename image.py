import cv2
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.preprocessing import scale

import plots as pl

class Image:
    def __init__(self, path = "test_photo.png"):
        self.load_image(path)

    def load_image(self, path):
        """
        :param path: string containing path to image
        :return: numpy array containg image
        """
        self.image_array = cv2.imread(path, 0)
        if self.image_array is None:
            print("Wrong image-path")
            raise TypeError

    def extract_coordinates(self):
        """
        Extracts indexes of dark spots on image
        """
        x, y = np.where(self.image_array < 255 / 3)
        [x_dim, y_dim] = self.image_array.shape
        # Converting so that 0 is at the bottom instead of the first row
        x = np.ones(len(x)) * (self.image_array.shape[0] - 1) - x
        # Making sure the lovest part of x is 0
        x = x - min(x)
        df = pd.DataFrame({"y_list": x, "x_list": y})
        df.sort_values(by="x_list", inplace=True)
        self.extracted_x = df.x_list.values / x_dim
        self.extracted_y = df.y_list.values / y_dim

    def interpolate_coordinates(self):
        #print("x min and max:", min(x), max(x))
        #print("y min and max: ", min(y), max(y))
        #Reduce number of points to interpolate to ensure smoother function
        self.extracted_x = self.extracted_x[::3]
        self.extracted_y = self.extracted_y[::3]
        #print("length of x and y are now:", len(x), len(y))
        #Create interpolation object
        f = interp1d(self.extracted_x, self.extracted_y, kind='linear', assume_sorted=True, bounds_error=False, fill_value='extrapolate')
        #self.unique_x = np.linspace(min(x), max(x), 100)
        #self.f_x = f1(self.unique_x)
        #print("x list: ", self.unique_x)
        #print("f(x) list: ", self.f_x)
        #pl.plot_array(self.unique_x, self.f_x)
        return f
