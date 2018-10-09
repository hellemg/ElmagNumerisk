import numpy as np
import scipy.integrate as integr


class Potential:
    def __init__(self, func):
        self.a = 0  # Start of integration-interval, in both potential and Fourier coefficients
        self.b = 1  # End of integration-interval, in both potential and Fourier coefficients
        self.tol = 10 ** (-6) #Error tolerance. Might not need for this part
        self.number_of_x = 101 #Number of points in x-array (I think)
        self.x_array = np.linspace(self.a, self.b, self.number_of_x)
        self.y_array = self.x_array.copy()
        self.func = func(self.x_array)  # V0: numpy array, function of potential

    def fourier(self, n):
        """
        :param n: int, term in Fourier coeffs
        :return: Function in the Fourier coeffs (check out what I meant by this)
        """
        return self.func * np.sin(n * np.pi * self.x_array)


    def simpson(self, f):
        """
        :param f: function to integrate
        :return: integrated function by Simpsons Method
        """
        return integr.simps(f, self.x_array)


    def coeff_n(self, n):
        """
        :param n: int, term in Fourier
        :return: Current coefficient
        """
        # Return: Current coefficient n
        return 2 / (np.sinh(n * np.pi)) * self.simpson(self.fourier(n))

    def set_y(self, y):
        """
        :param y: numpy array
        """
        self.y_array = y

    def make_two_dim(self):
        self.x_array, self.y_array = np.meshgrid(self.x_array, self.y_array)  # mesh-smesh

    def approximate_potential(self, n):
        """
        :param n: int, term in Fourier
        :return: numpy array, approximation of potential for Fourier term n
        """
        return self.coeff_n(n) * np.sinh(n * np.pi * self.y_array) * np.sin(n * np.pi * self.x_array)

    def total_potential(self, N, two_dims = False):
        """
        :param N: int, number of Fourier terms to approximate for
        :param two_dims: boolean, two dims or not. Not means one dim
        :sets: self.z
        """
        if two_dims:
            self.z = np.zeros((self.number_of_x, self.number_of_x))
        else:
            self.z = np.zeros(self.number_of_x)
        for n in range(1, N):
            self.z += self.approximate_potential(n)

