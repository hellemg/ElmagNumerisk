import functions as fun
import numpy as np
import matplotlib.pyplot as plt
import unittest

import plots as pl


if __name__ == '__main__':
    # Endrer MasterFlag for å få kjørt ønsket kode
    MasterFlag = {
        -1: 'Testspace',
        0: 'Boundary 4',
        1: 'Plot contour V',
        2: 'Boundaries 1-3',
        3: 'Error',
        4: 'Electric field'
    }[-1]
    if MasterFlag == 'Testspace':
        print('Welcome to testspace')
        from test import *

        unittest.main()

    elif MasterFlag == 'Boundary 4':
        N = 200  # Number of Fourier terms to approximate for
        y_list = np.linspace(0, 1, fun.X_es)  # y-values at which to evaluate the potential
        x_list = np.linspace(0, 1, fun.X_es)  # x-values at which to evaluate the potential
        one_list = np.ones_like(y_list)
        V0_a = fun.V0_choices('a')
        V_a = fun.total_potential(x_list, one_list, V0_a, N)  # x, y=1
        V0_b = fun.V0_choices('b')
        V_b = fun.total_potential(x_list, one_list, V0_b, N)  # x, y=1
        V0_c = fun.V0_choices('c')
        V_c = fun.total_potential(x_list, one_list, V0_c, N)  # x, y=1
        V0_d = fun.V0_choices('d')
        V_d = fun.total_potential(x_list, one_list, V0_d, N)  # x, y=1
        pl.plot_boundary4(x_list, V_a, V_b, V_c, V_d, V0_a, V0_b, V0_c, V0_d)

    elif MasterFlag == 'Plot contour V':
        N = 200  # Number of Fourier terms to approximate for
        x_list = np.linspace(0, 1, fun.X_es)  # x-values at which to evaluate the potential
        y_list = np.linspace(0, 1, fun.X_es)  # y-values at which to evaluate the potential
        xx, yy = np.meshgrid(x_list, y_list)  # mesh-smesh
        V0 = np.array([fun.V0_choices('a'), fun.V0_choices('b'), fun.V0_choices('c'), fun.V0_choices('d')])  # Potential choices: a, b, c, d
        Z_a = fun.total_potential(xx, yy, V0[0], N, True)  # Calculate potential for whole area
        Z_b = fun.total_potential(xx, yy, V0[1], N, True)  # Calculate potential for whole area
        Z_c = fun.total_potential(xx, yy, V0[2], N, True)  # Calculate potential for whole area
        Z_d = fun.total_potential(xx, yy, V0[3], N, True)  # Calculate potential for whole area
        pl.contour_plot(xx, yy, Z_a, Z_b, Z_c, Z_d)  # Plot the potential for whole area

    elif MasterFlag == 'Boundaries 1-3':
        N = 200  # Number of Fourier terms to approximate for
        y_list = np.linspace(0, 1, fun.X_es)  # y-values at which to evaluate the potential
        x_list = np.linspace(0, 1, fun.X_es)  # x-values at which to evaluate the potential
        zero_list = np.zeros_like(y_list)
        one_list = np.ones_like(y_list)
        V0 = fun.V0_choices('c')
        V_x0 = fun.total_potential(zero_list, y_list, V0, N)  # x=0, y
        V_y0 = fun.total_potential(x_list, zero_list, V0, N)  # x, y=0
        V_x1 = fun.total_potential(one_list, y_list, V0, N)  # x=1, y
        V_y1 = fun.total_potential(x_list, one_list, V0, N)  # x, y=1
        pl.plot_boundaries(x_list, V_x0, V_x1, V_y0, np.zeros_like(V0))
        # These are alle zero
        # error_x0 = np.linalg.norm(zero_list - Vx0, np.Inf)
        # error_y0 = np.linalg.norm(zero_list - Vy0, np.Inf)
        # error_x1 = np.linalg.norm(zero_list - Vx1, np.Inf)

    elif MasterFlag == 'Error':
        N_list, error_list_a, error_list_b, error_list_c, error_list_d = fun.get_errors(220)  # Input: N_max, V0_choice
        pl.plot_error(N_list, error_list_a, error_list_b, error_list_c, error_list_d)
        plt.show()

    elif MasterFlag == 'Electric field':
        N = 200
        x_list = np.linspace(0, 1, fun.X_es)  # x-values at which to evaluate the potential
        y_list = np.linspace(0, 1, fun.X_es)  # y-values at which to evaluate the potential
        xx, yy = np.meshgrid(x_list, y_list)
        V0 = np.array([fun.V0_choices('a'), fun.V0_choices('b'), fun.V0_choices('c'), fun.V0_choices('d')])  # Potential choices: a, b, c, d
        Z_a = fun.total_potential(xx, yy, V0[0], N, two_dim=True)  # Calculate potential for whole area
        Z_b = fun.total_potential(xx, yy, V0[1], N, two_dim=True)  # Calculate potential for whole area
        Z_c = fun.total_potential(xx, yy, V0[2], N, two_dim=True)  # Calculate potential for whole area
        Z_d = fun.total_potential(xx, yy, V0[3], N, two_dim=True)  # Calculate potential for whole area
        field_a = fun.field(Z_a)
        field_b = fun.field(Z_b)
        field_c = fun.field(Z_c)
        field_d = fun.field(Z_d)
        pl.plot_electricField(xx, yy, -field_a[0], -field_a[1], -field_b[0], -field_b[1], -field_c[0], -field_c[1], -field_d[0], -field_d[1])
