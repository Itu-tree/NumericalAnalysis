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
ylist = []
conx = np.empty(0)
cony = np.empty(0)
for t in np.linspace(0.001, 1, 50):
    y = -np.sqrt(1-t**2)/t * x + np.sqrt(1-t**2)
    plt.ylim([0,1])
    conx = np.hstack((conx,x))
    cony = np.hstack((cony,y))
    im = plt.plot(conx,cony)
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save("envelope_traje.mp4", writer="ffmpeg",dpi=300) 
