#-- coding:utf-8 --
#波動方程式

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm
N = 10

fig = plt.figure()
ims = []
time = 101
x = np.linspace(0,np.pi,N)
ylist = []
ylist.append(np.sin(x))
alpha = 1/3

for t in tqdm(range(1,time)):
    newy = np.zeros(N)
    if t == 1:
        for i in range(x.size):
            if i == 0 or i == x.size-1:
                newy[i] = 0
            else:
                newy[i] = ylist[0][i] + (ylist[0][i+1]+ylist[0][i-1]-2*ylist[0][i])*alpha/2
    else:
        for i in range(x.size):
            if i == 0 or i == x.size-1:
                newy[i] = 0
            else:
                newy[i] = 2*ylist[t-1][i]-ylist[t-2][i]+(ylist[t-1][i+1]+ylist[t-1][i-1]-2*ylist[t-1][i])*alpha
    #print(newy)
    ylist.append(newy)

for i in tqdm(ylist):
    plt.ylim(-1.5,1.5)
    ims.append(plt.plot(x,i,color='blue'))

ani = animation.ArtistAnimation(fig, ims)
ani.save("ani2.mp4", writer="ffmpeg",dpi=300) 
#ani.save("ani2.gif", writer="imagemagick") 

