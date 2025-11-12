import numpy as np
import matplotlib.pyplot as plt

# Sample trajectory
x = np.linspace(0, 10, 100)
y = 5 * x

def location(xs, ys):
    """Yield successive (x, y) targets along the path."""
    for xi, yi in zip(xs, ys):
        yield xi, yi

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(x.min() - 1, x.max() + 1)
ax.set_ylim(y.min() - 1, y.max() + 1)
ax.set_xlabel("x")
ax.set_ylabel("y")
tracker = ax.scatter([], [], s=80, color="crimson")


for i, j in location(x, y):
    tracker.set_offsets([[i, j]])  # move marker instead of creating new figure
    fig.canvas.draw_idle()
    plt.pause(0.1)

plt.ioff()
plt.show()
