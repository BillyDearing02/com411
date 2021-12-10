# imports plotting and animation modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# draws the plots for each frame
def animate(frame):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')
# calls the animate function
ani = FuncAnimation(fig, animate, frames=10, interval=100)
# shows the plot
plt.show()




