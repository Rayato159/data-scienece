import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function and its derivative
def f(x):
    return x ** 2

def df(x):
    return 2 * x

# Calculate tangent line based on the slope and a point
def tangent_line(x, x_point, y_point):
    slope = df(x_point)
    return slope * (x - x_point) + y_point

# Initialize parameters
x_start = -10  # Starting value of x
learning_rate = 0.1
n_iterations = 50

# Set up the figure, the axis, and the plot elements we want to animate
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 400)
ax.plot(x, f(x), 'b-', label='f(x) = x^2')
point, = ax.plot([], [], 'ro', label='Current point')
line, = ax.plot([], [], 'g-', label='Tangent line at current point')
value_display = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    line.set_data([], [])
    value_display.set_text('')
    return point, line, value_display

# Animation update function
def update(i):
    global x_start
    # Reset x_start after finishing the iterations to loop
    if i == 0:
        x_start = -10
    x_start -= learning_rate * df(x_start)
    y = f(x_start)
    y_tangent = tangent_line(x, x_start, y)
    
    point.set_data(x_start, y)
    line.set_data(x, y_tangent)
    value_display.set_text(f'Value = {y:.2f} at x = {x_start:.2f}')
    return point, line, value_display

# Call the animator
ani = FuncAnimation(fig, update, frames=np.arange(0, n_iterations), init_func=init, repeat=True)

plt.show()
