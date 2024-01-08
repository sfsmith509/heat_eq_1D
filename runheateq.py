import numpy as np 
from heatequation import *
from matplotlib import animation, pyplot as plt

#set variables
x    = np.linspace(0, np.pi, 20)
f    = lambda x,t: np.e**(-t)*np.sin(x) +2
t0   = 0
dx   = x[1] - x[0]
r    = .49 # forward Euler method r can be as high as .5 
dt   = r*(dx**2)
u0   = f(x, t0)
u    = u0
time = t0

#plot figure
fig = plt.figure()
ax = plt.axes(xlim=(0,np.pi), ylim=(2,3))
#ax.set_axis_bgcolor('yellow')
ax.set_xlabel('X')
ax.set_ylabel('u(x,t) = Temperature')
line, = ax.plot([], [], lw=1)
#100 time steps plot animation
for i in range(200):
    nr_times = 1
    u, time = EulerHeatConstBC(u, x, dt, nr_times, time)
    line.set_data(x, u)
    plt.savefig(str("{0:03}".format(i))+'.png')
