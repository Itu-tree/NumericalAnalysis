"""
直線群を表示し、包絡線を示します（軌跡あり）

曲線群 f(x,y,t)=0 の包絡線の方程式は f(x,y,t)=0 と 
∂∂tf(x,y,t)=0 から t を消去することで得られる。

"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig = plt.figure()
ims = []
# パラメーター
t1 = -2
t2 = 2
tstep = 50
#定義域
x1 = -3
x2 = 3
xstep = 100
# 値域
y1 = -3
y2 = 3

def f(x,t): 
    # 曲線（直線）群 
    #y = 2*t*x-t**2 # y = x**2
    #y = 2/5*t*x - 1/5*t**2 # y = 1/5*x**2
    #y = -np.sqrt(1-t**2)/t * x + np.sqrt(1-t**2)
    #y = t*x**2 + (1-4*t**2)/4/t
    y = (3*t**2-1)*x -2*t**3
    return y

graph_size = 10
plt.rcParams['figure.figsize'] = (graph_size, graph_size)
#plt.axis('off')

x = np.linspace(x1,x2,xstep) # 定義域,分割数
ylist = []
conx = np.empty(0)
cony = np.empty(0)
for t in np.linspace(t1, t2, tstep): # 曲線（直線）の数
    y = f(x,t)
    plt.ylim([y1,y2]) # 値域
    conx = np.hstack((conx,x))
    cony = np.hstack((cony,y))
    im = plt.plot(conx,cony)
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save("envelope_y-eq3t21x2t3.mp4", writer="ffmpeg",dpi=300) 
