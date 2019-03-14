"""
包絡線を表示します（軌跡なし）

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig = plt.figure()
ims = []
#f(x,y,t) 包絡線

graph_size = 10
plt.rcParams['figure.figsize'] = (graph_size, graph_size)
#plt.axis('off')

x = np.linspace(0,1,100)

for t in np.linspace(0.001, 1, 50):
    y = -np.sqrt(1-t**2)/t * x + np.sqrt(1-t**2)
    plt.ylim([0,1])
    im = plt.plot(x,y)
    ims.append(im)


ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save("envelope_notraje.mp4", writer="ffmpeg",dpi=300) 
#plt.show()