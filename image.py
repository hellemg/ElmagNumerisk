import cv2
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.preprocessing import scale

import plots as pl

class Image:
    def __init__(self, track_progress= True, path = "test_photo.png"):
        self.track_progress = track_progress
        self.load_image(path)


    def load_image(self, path):
        """
        :param path: string containing path to image
        :return: numpy array containg image
        """
        if self.track_progress:
            print("loading image...", end = " ")
        self.image_array = cv2.imread(path, 0)
        if self.image_array is None:
            print("Wrong image-path")
            raise TypeError
        if self.track_progress:
            print("OK")

    def extract_coordinates(self):
        """
        Extracts indexes of dark spots on image
        """
        if self.track_progress:
            print("extracting coordinates...", end = " ")
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
        if self.track_progress:
            print("OK")

    def interpolate_coordinates(self):
        """
        Interpolates the function gives by image
        :return: f: interpolation object, works as a function
        """
        if self.track_progress:
            print("interpolating coordinates...", end = " ")
        #Reduce number of points to interpolate to ensure smoother function
        self.extracted_x = self.extracted_x[::3]
        self.extracted_y = self.extracted_y[::3]
        #Create interpolation object
        f = interp1d(self.extracted_x, self.extracted_y, kind='linear', assume_sorted=True, bounds_error=False, fill_value='extrapolate')
        if self.track_progress:
            print("OK")
        return f
