import functions as fun
import numpy as np
import matplotlib.pyplot as plt

import plots as pl

if __name__ == '__main__':
    # Endrer MasterFlag for å få kjørt ønsket kode
    MasterFlag = {
        -1: 'Testspace',
        0: 'Convergence_test',
        1: 'Plot contour V',
        2: 'Plot boundary',
        3: 'Electric field'
    }[3]
    if MasterFlag == 'Testspace':
        print('Hello')
    elif MasterFlag == 'Convergence_test':
        fun.convergence()
    elif MasterFlag == 'Plot contour V':
        N = 100  # Number of points to evaluate in an integration. #panels = N-1
        x_list = np.linspace(0, 1, fun.X_es)  # x-values at which to evaluate the potential
        y_list = np.linspace(0, 1, fun.X_es)  # y-values at which to evaluate the potential
        xx, yy = np.meshgrid(x_list, y_list)
        V0 = fun.V0_choices('a')
        z = fun.total_potential1(xx, yy, V0, N)
        pl.contour_plot(xx, yy, z, V0)
        # z_one = fun.total_potential(x_list, np.ones_like(x_list), V0, N)
        # plt.plot(x_list, z_one)
        plt.show()
    elif MasterFlag == 'Plot boundary':
        N_list, error_list = fun.plot_boundary()
        plt.plot(N_list, error_list)
        plt.show()
    elif MasterFlag == 'Electric field':
        N = 200
        x_list = np.linspace(0, 1, fun.X_es)  # x-values at which to evaluate the potential
        y_list = np.linspace(0, 1, fun.X_es)  # y-values at which to evaluate the potential
        xx, yy = np.meshgrid(x_list, y_list)
        V0 = fun.V0_choices('c')
        z = fun.total_potential1(xx, yy, V0, N)
        pl.contour_plot(xx, yy, z, V0)
        field = fun.field(z)
        #x_sliced = np.linspace(0, 1, 50)
        #y_sliced = np.linspace(0, 1, 50)
        #xx_sliced, yy_sliced = np.meshgrid(x_sliced, y_sliced)
        plt.quiver(xx, yy, -field[0], -field[1], )
        plt.show()