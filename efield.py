import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

fig = plt.figure()
ims = []

# 定数
Q = (((0,0),10),((5,-5),5))
FINISHTIME = 20
RLIMIT = 0.1
H = 0.01
M = 1
k = 1
q = -1


for qi in Q:
    plt.plot(qi[0][0],qi[0][1],".")

t = 0

# 初期値の入力
x = float(input("x0 を入力してください : x0 = "))
y = float(input("y0 を入力してください : y0 = "))
vx = float(input("v0x を入力してください : v0x = "))
vy = float(input("v0y を入力してください : v0y = "))

print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t,x,y,vx,vy))

xlist = [x]
ylist = [y]


while t < FINISHTIME:
    t = t + H
    rmin = float("inf")
    for qi in Q:
        rx = x - qi[0][0]
        ry = y - qi[0][1]
        r = math.sqrt(rx**2 + ry**2)
        if r < rmin:
            rmin = r
        
        vx += (k*q*rx/r/r/r*qi[1])*H
        vy += (k*q*ry/r/r/r*qi[1])*H
    x += vx*H
    y += vy*H
    xlist.append(x)
    ylist.append(y)
    if rmin < RLIMIT:
        break
    
    im = plt.plot(xlist,ylist,color = "b")
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=10)

#ani.save("MovementOfCharge.gif", writer="imagemagick") 
ani.save("MovemtenoOfCharge.mp4", writer="ffmpeg",dpi=300) 
#ani.save('MoveOfCharge.gif', writer='pillow') # fpsはデフォルトの5
#plt.plot(xlist,ylist)
#plt.show()