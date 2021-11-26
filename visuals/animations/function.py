import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frames):
    global ax
    x = []
    x_num = 0
    x_num = x_num + 1
    x.append(x_num)
    x_num = x_num + 1
    x.append(x_num)
    y = []
    y_num = 0
    y_num = y_num + 1
    y.append(y_num)
    print(f"The current frame number is: {frames}")
    ax.plot(x, y)


some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
plt.show()


