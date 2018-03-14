from datetime import datetime

import matplotlib.pyplot as plt

def contour_plot(X, Y, Z_a, Z_b, Z_c, Z_d):
    plt.suptitle(r'Relative potentials $V(\varepsilon, \delta)/V_c$', fontsize=20)

    plt.subplot(221)
    plt.contourf(X, Y, Z_a)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$V_0(\varepsilon)=V_{0,a}(\varepsilon)$', fontsize=10)

    plt.subplot(222)
    plt.contourf(X, Y, Z_b)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$V_0(\varepsilon)=V_{0,b}(\varepsilon)$', fontsize=10)

    plt.subplot(223)
    plt.contourf(X, Y, Z_c)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$V_0(\varepsilon)=V_{0,c}(\varepsilon)$', fontsize=10)

    plt.subplot(224)
    plt.contourf(X, Y, Z_d)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$V_0(\varepsilon)=V_{0,d}(\varepsilon)$', fontsize=10)

    plt.tight_layout(rect=[0, 0.03, 0.99, 0.93])
    #plt.show()
    plt.savefig(datetime.now().strftime('Potentials.pdf'))

'''
def plot_BCs(x, y):
    plt.plot(x, y, color='lime', label='Potential for BC 1-3')
    plt.show()
'''
'''
def plot_BC4(x, y, V0):
    plt.plot(x, y, color='fuchsia', label=r'Numerical potential $V_{num}$')
    plt.plot(x, V0, color='lime', linestyle='--', label='Analytic potential')
    plt.title('Do I even use this?')
    plt.show()
'''

def plot_error(N_list, error_list_a, error_list_b, error_list_c, error_list_d):
    plt.plot(N_list, error_list_a, color='r', label=r'$V_0(\varepsilon)=V_{0,a}(\varepsilon)$')
    plt.plot(N_list, error_list_b, color='b', label=r'$V_0(\varepsilon)=V_{0,b}(\varepsilon)$')
    plt.plot(N_list, error_list_c, color='y', label=r'$V_0(\varepsilon)=V_{0,c}(\varepsilon)$')
    plt.plot(N_list, error_list_d, color='g', label=r'$V_0(\varepsilon)=V_{0,d}(\varepsilon)$')
    plt.ylabel(r'Error')
    plt.xlabel(r'$N$')
    plt.legend(fontsize='x-small', loc=4)

    plt.title(r'Relative errors as a function of Fourier orders $N$', fontsize=15)
    #plt.show()
    plt.savefig(datetime.now().strftime('RelativeErrors.pdf'))

def plot_boundaries(dist, V_x0, V_x1, V_y0, V0_zeros):
    plt.suptitle(r'Relative potentials for $V_0(\varepsilon)=V_{0, c}$', fontsize=20)
    plt.subplot(311)
    plt.plot(dist, V_x0, label='Numerical', color='cyan')
    plt.plot(dist, V0_zeros, '--', label='Analytical')
    plt.ylim(-0.5, 3.5)
    plt.yticks([0, 1, 2, 3])
    plt.ylabel(r'$V(0, \delta)/V_c$', fontsize=7)
    plt.xlabel(r'$\delta$', fontsize=7)
    plt.tick_params(labelsize=5)
    plt.legend(fontsize='x-small')
    plt.title(r'Relative potential at $(0, \delta)$', fontsize=7)
    plt.subplot(312)
    plt.plot(dist, V_x1, label='Numerical', color='cyan')
    plt.plot(dist, V0_zeros, '--', label='Analytical')
    plt.ylim(-0.5, 3.5)
    plt.yticks([0, 1, 2, 3])
    plt.ylabel(r'$V(1, \delta)/V_c$', fontsize=7)
    plt.xlabel(r'$\delta$', fontsize=7)
    plt.tick_params(labelsize=5)
    plt.legend(fontsize='x-small')
    plt.title(r'Relative potential at $(1, \delta)$', fontsize=7)
    plt.subplot(313)
    plt.plot(dist, V_y0, label='Numerical', color='cyan')
    plt.plot(dist, V0_zeros, '--', label='Analytical')
    plt.ylim(-0.5, 3.5)
    plt.yticks([0, 1, 2, 3])
    plt.ylabel(r'$V(\varepsilon, 0)/V_c$', fontsize=7)
    plt.xlabel(r'$\varepsilon$', fontsize=7)
    plt.tick_params(labelsize=5)
    plt.legend(fontsize='x-small')
    plt.title(r'Relative potential at $(\varepsilon, 0)$', fontsize=7)
    '''
    plt.subplot(224)
    plt.plot(dist, V_y1, label='Numerical', color='cyan')
    plt.plot(dist, V0, '--', label='Analytical')
    plt.ylabel(r'$V(\varepsilon, 1)/V_c$', fontsize=7)
    plt.xlabel(r'$\varepsilon$', fontsize=7)
    plt.tick_params(labelsize=5)
    #plt.yticks([0, 1, 2, 3])
    plt.legend(fontsize='x-small', loc=4)
    plt.title(r'Relative potential at $(\varepsilon, 1)$', fontsize=8)
    '''
    plt.tight_layout(rect=[0, 0.03, 0.99, 0.93])
    #plt.show()
    plt.savefig(datetime.now().strftime('Boundaries13.pdf'))


def plot_electricField(xx, yy, Ex_a, Ey_a, Ex_b, Ey_b, Ex_c, Ey_c, Ex_d, Ey_d):
    plt.suptitle(r'Electric fields $E(\varepsilon, \delta)$', fontsize=20)

    plt.subplot(221)
    plt.streamplot(xx, yy, Ex_a, Ey_a)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$E(\varepsilon, \delta)$ from $V_0(\varepsilon)=V_{0,a}(\varepsilon)$', fontsize=10)

    plt.subplot(222)
    plt.streamplot(xx, yy, Ex_b, Ey_b)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$E(\varepsilon, \delta)$ from $V_0(\varepsilon)=V_{0,b}(\varepsilon)$', fontsize=10)

    plt.subplot(223)
    plt.streamplot(xx, yy, Ex_c, Ey_c)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$E(\varepsilon, \delta)$ from $V_0(\varepsilon)=V_{0,c}(\varepsilon)$', fontsize=10)

    plt.subplot(224)
    plt.streamplot(xx, yy, Ex_d, Ey_d)
    plt.xlabel(r'$\varepsilon$')
    plt.ylabel(r'$\delta$')
    plt.tick_params(labelsize=5)
    plt.title(r'$E(\varepsilon, \delta)$ from $V_0(\varepsilon)=V_{0,d}(\varepsilon)$', fontsize=10)

    plt.tight_layout(rect=[0, 0.03, 0.99, 0.93])
    #plt.show()
    plt.savefig(datetime.now().strftime('ElectricField.pdf'))



def plot_boundary4(dist, V_a, V_b, V_c, V_d, V0_a, V0_b, V0_c, V0_d):
    plt.subplot(221)
    plt.plot(dist, V_a, label='Numerical', color='cyan')
    plt.plot(dist, V0_a, '--', label='Analytical')
    plt.ylabel(r'$V(\varepsilon, 1)/V_c$', fontsize=7)
    plt.xlabel(r'$\varepsilon$', fontsize=7)
    plt.tick_params(labelsize=5)
    plt.yticks([-1, -0.5, 0, 1, 0.5, 1])
    plt.legend(fontsize='x-small', loc=0)
    plt.title(r'$V_0(\varepsilon)=V_{0,a}(\varepsilon)$', fontsize=10)

    plt.subplot(222)
    plt.plot(dist, V_b, label='Numerical', color='cyan')
    plt.plot(dist, V0_b, '--', label='Analytical')
    plt.ylabel(r'$V(\varepsilon, 1)/V_c$', fontsize=7)
    plt.xlabel(r'$\varepsilon$', fontsize=7)
    plt.tick_params(labelsize=5)
    #plt.yticks([0, 1, 2, 3])
    plt.legend(fontsize='x-small', loc=0)
    plt.title(r'$V_0(\varepsilon)=V_{0,b}(\varepsilon)$', fontsize=10)

    plt.subplot(223)
    plt.plot(dist, V_c, label='Numerical', color='cyan')
    plt.plot(dist, V0_c, '--', label='Analytical')
    plt.ylabel(r'$V(\varepsilon, 1)/V_c$', fontsize=7)
    plt.xlabel(r'$\varepsilon$', fontsize=7)
    plt.tick_params(labelsize=5)
    #plt.yticks([0, 1, 2, 3])
    plt.legend(fontsize='x-small', loc=0)
    plt.title(r'$V_0(\varepsilon)=V_{0,c}(\varepsilon)$', fontsize=10)

    plt.subplot(224)
    plt.plot(dist, V_d, label='Numerical', color='cyan')
    plt.plot(dist, V0_d, '--', label='Analytical')
    plt.ylabel(r'$V(\varepsilon, 1)/V_c$', fontsize=7)
    plt.xlabel(r'$\varepsilon$', fontsize=7)
    plt.tick_params(labelsize=5)
    #plt.yticks([0, 1, 2, 3])
    plt.legend(fontsize='x-small', loc=0)
    plt.title(r'$V_0(\varepsilon)=V_{0,d}(\varepsilon)$', fontsize=10)

    plt.suptitle(r'Relative potentials $V(\varepsilon, 1)/V_c$', fontsize=20)
    plt.tight_layout(rect=[0, 0.03, 0.99, 0.93])
    #plt.show()
    plt.savefig(datetime.now().strftime('Boundary4.pdf'))
