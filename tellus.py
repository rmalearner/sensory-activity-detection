import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

csv = pd.read_csv("data.csv")

max_pir = max(csv["pir"])
min_pir = min(csv["pir"])

x_progress = []
y_progress = []

mul_fac = 5000

fig = plt.figure()
ax = plt.axes(xlim=(0, csv.shape[0]), ylim=(min_pir, max_pir))
ax.axes.get_xaxis().set_visible(False)
line, = ax.plot(x_progress, y_progress, lw=1)

index = 0

def animate(i):
    global x_progress
    global y_progress
    global index

    index = i * mul_fac

    if index >= csv.shape[0]:
        return line,

    pir = csv.loc[csv.index[index:(index + mul_fac)], "pir"].max()
    timestamp = csv.loc[csv.index[index], "timestamp"]

    x_progress += [index]
    y_progress += [pir]

    line.set_data(x_progress, y_progress)
    plt.title(timestamp)
    
    return line,

anim = animation.FuncAnimation(fig, animate, frames=csv.shape[0] // mul_fac, interval=1, repeat=False)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=24, metadata=dict(artist='Rohit Mishra'), bitrate=1800)
anim.save('output.mp4', writer=writer)
