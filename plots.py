import functions as fun
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integr

def contour_plot(X, Y, Z, V0an):
    plt.figure()
    #CS = plt.contourf(X, Y, Z)
    #CS = plt.contourf(X, Y, V0an)
    #plt.clabel(CS, inline=1, fontsize=10)
    plt.contourf(X, Y, Z)
    plt.title('V(x, y)')
    plt.show()

def plot_BCs(x, y):
    plt.plot(x, y, color='magenta', label='Potential for BC 1-3')
    plt.show()


def plot_BC4(x, y, V0, leg):
    plt.plot(x, y, color='fuchsia', label='Numerical potential $V_{num}$')
    plt.plot(x, V0, color='lime', linestyle='--', label='Analytic potential')
    #plt.ylim(-1, 10)
    plt.title(leg)
    plt.show()



def plot_error(n, error):
    plt.plot(n, error, color='fuchsia', label='Error')
    plt.title('Error as a function of number of Fourier orders')
    plt.show()

def plot_sev(N_list, error_x0num, error_y0num, error_x1num, error_y1num):
    plt.plot(N_list, error_x0num, color='fuchsia')
    plt.plot(N_list, error_y0num, color='darkblue')
    plt.plot(N_list, error_x1num, color='green')
    plt.plot(N_list, error_y1num, color='cyan')
    plt.title('Errors at boundaries as functions of N')
    plt.show()