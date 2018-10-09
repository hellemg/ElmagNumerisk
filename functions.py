import numpy as np
import scipy.integrate as integr

a = 0  # Start of integration-interval, in both potential and Fourier coefficients
b = 1  # End of integration-interval, in both potential and Fourier coefficients
tol = 10 ** (-6)
X_es = 1001
x_list = np.linspace(a, b, X_es)


def fourier(n, V0):
    # Function in the Fourier coeffs
    # Input: Current n, potential list V0
    return V0 * np.sin(n * np.pi * x_list)


def simpson(f):
    # Integrates the function f
    # Input: Function
    # Return: Integrated function
    return integr.simps(f, x_list)


def coeff_n(n, V0):
    # Input: Current n, potential list V0
    # Return: Current coefficient n
    return 2 / (np.sinh(n * np.pi)) * simpson(fourier(n, V0))


'''Everything above this are constants when put toghether in coeff_n'''


# Set potential with a dictionary for easy change
# Returns V0(x)/Vc
def V0_choices(choice):
    return {
        'a': np.sin(3 * np.pi * x_list),
        'b': 1 - (x_list - 1 / 2) ** 4,
        'c': np.heaviside(x_list - 1 / 2, 1) * np.heaviside(3 / 4 - x_list, 1),
        'd': np.ones_like(x_list) * 20
    }.get(choice, 1)  # 1 is default if x not found


def potential_n(n, x, y, V0):
    # Input: Current n, list of x-values, list of y-values
    # Return: Potential for current n
    return coeff_n(n, V0) * np.sinh(n * np.pi * y) * np.sin(n * np.pi * x)


def total_potential(x, y, V0, N, two_dim = False):
    if not two_dim:
        z = np.zeros(X_es)
    else:
        z = np.zeros((X_es, X_es))
    for n in range(1, N):
        z += potential_n(n, x, y, V0)
    return z


def get_errors(N_max):
    error_list_a = np.array([])
    error_list_b = np.array([])
    error_list_c = np.array([])
    error_list_d = np.array([])
    N_list = np.array([])
    for N in range(1, N_max):
        x_list = np.linspace(0, 1, X_es)  # x-values at which to evaluate the potential
        V0 = np.array([V0_choices('a'), V0_choices('b'), V0_choices('c'), V0_choices('d')])
        V_a = total_potential(x_list, np.ones_like(x_list), V0[0], N)  # x, y=1
        V_b = total_potential(x_list, np.ones_like(x_list), V0[1], N)  # x, y=1
        V_c = total_potential(x_list, np.ones_like(x_list), V0[2], N)  # x, y=1
        V_d = total_potential(x_list, np.ones_like(x_list), V0[3], N)  # x, y=1

        error_a = np.linalg.norm(V0[0] - V_a, np.Inf) / np.linalg.norm(V0[0], np.Inf)
        error_b = np.linalg.norm(V0[1] - V_b, np.Inf) / np.linalg.norm(V0[1], np.Inf)
        error_c = np.linalg.norm(V0[2] - V_c, np.Inf) / np.linalg.norm(V0[2], np.Inf)
        error_d = np.linalg.norm(V0[3] - V_d, np.Inf) / np.linalg.norm(V0[3], np.Inf)

        error_list_a = np.append(error_list_a, error_a)
        error_list_b = np.append(error_list_b, error_b)
        error_list_c = np.append(error_list_c, error_c)
        error_list_d = np.append(error_list_d, error_d)

        N_list = np.append(N_list, N)
    return N_list, error_list_a, error_list_b, error_list_c, error_list_d


def field(V_num):
    return np.gradient(V_num)


'''
    def boundary_potential(x, y, V0, N):
        if x[10] == 0:
            print('welcome to x=0')
            V = total_potential(np.zeros(len(y)), y, V0, N)
            plotting = "V(0, y), should be 0"
        elif y[10] == 0:
            V = total_potential(x, np.zeros(len(x)), V0, N)
            plotting = "V(x, 0), should be 0"
        elif x[10] == 1:
            V = total_potential(np.ones(len(y)), y, V0, N)
            plotting = "V(1, y), should be 0"
        elif y[10] == 1:
            V = total_potential(x, np.ones(len(x)), V0, N)
            plotting = "V(x, 1), should be V0"
        print('list: ', list, 'V: ', V, 'plotting: ', plotting)
        return V, plotting
'''
