import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()

ims = []

x = np.linspace(0,10*np.pi,1000)
for i in range(100):
        
        y = np.sin(x+i*np.pi/20)
        im = plt.plot(x,y,color="black",linestyle = "--")   
        plt.title("sin wave")
        plt.xlabel("x")
        plt.ylabel("y")

        ims.append(im)                  # グラフを配列 ims に追加


# 10枚のプロットを 100ms ごとに表示
ani = animation.ArtistAnimation(fig, ims, interval=50)
# 
# plt.show()

# gifでの保存にはmatplotlibにimagemagickのパスが通っている必要がある
#ani.save("sin_anim.gif", writer="imagemagick") 

# mp4での保存にはffpmegのパスが通っている必要がある
ani.save("sin_anim.mp4", writer="ffmpeg",dpi=300) 