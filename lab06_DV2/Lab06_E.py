from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import math

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

trace, = ax.plot([], [], '-', lw=2, color='orange', alpha=1.0)
tail, = ax.plot([], [], '-', lw=2, color='orange', alpha=0.3)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

"""
1) Plot the trace in the animation -> set max_trace_length = math.inf
2) Keep the trace in a fixed length -> set max_trace_length = 20
3) Adjust the transparency on the tail
    let alpha = 1.0 for trace
        alpha = 0.3 for tail

"""
max_trace_length = math.inf
# For 2) ,3) uncomment the below line
# max_trace_length = 30
x2_trace = []
y2_trace = []


max_tail_length = 0
# For 3) uncomment the below line
# max_tail_length = 5
x2_tail = []
y2_tail = []


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    x2_trace.append(x2[i])
    y2_trace.append(y2[i])

    if len(x2_trace) > max_trace_length:
        x2_tail.append(x2_trace.pop(0))
        y2_tail.append(y2_trace.pop(0))



    while len(x2_tail) > max_tail_length:
        x2_tail.pop(0)
        y2_tail.pop(0)


    trace.set_data(x2_trace, y2_trace)
    # x2_tail.insert(0, x2_trace[0])
    # y2_tail.insert(0, y2_trace[0])
    # x2_tail.pop(-1)
    # y2_tail.pop(-1)
    x2_tail.append(x2_trace[0])
    y2_tail.append(y2_trace[0])

    tail.set_data(x2_tail, y2_tail)
    
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                              interval=dt*1000, blit=False, init_func=init)
plt.show()