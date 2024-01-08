import numpy as np
#import matplotlib.pyplot as plt
#from scipy import *



# a 1D uniform insulating bar heat up, solving with finite difference methods

#discrtise the bar and equation 


# u temperature in bar funtion of x and t, u_t = u_xx
# u_i,j+1 = u_i,j + r(u_i+1,j -2u_i,j +u_i-1,j)sovle using Euler method


#the mesh

#boundary conditions at the ends of the bar here keep the ends of the bar cold


#matrix equation


def EulerHeatConstBC(u0, x, dt, nr_times, t0):
    #constants 
    t = t0
    dx = x[1] - x[0]
    r = dt/(dx**2)
    #length of initial array -2 on boundary 
    unknownu = len(u0) - 2
    mainDiag = -2*np.ones(unknownu)
    offDiag = np.ones(unknownu - 1)
    T = maketridiagmatrix(mainDiag, offDiag)
    u = u0




    #boundary conidtions set to first and last elements from initial array 
    BC = np.zeros(unknownu)
    BC[0] = u0[0]
    BC[-1] = u0[-1]



    #loop for solving heat equation
    #update elements on interia of bar, boundaries are fixed.
    for step in range(nr_times):
        u[1:-1] = u[1:-1] + r*np.dot(T, u[1:-1]) + r*BC
        t = t +dt
    return u, t



def maketridiagmatrix(main, offset):
    return np.diag(main) + np.diag(offset, k = -1) + np.diag(offset, k = 1)
