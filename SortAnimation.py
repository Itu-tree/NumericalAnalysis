import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from tqdm import tqdm

COLOR = "black"
N = 20
VALUEMAX = 50
VALUEMIN = 1
def BubbleSort(x,y,ims):
    for i in tqdm(range(0,N)):
        for j in range(i+1,N):
            if y[i] >= y[j]:
                y[i],y[j] = y[j],y[i]
                #plt.bar_list[i].set_color("blue")
                ims.append(plt.bar(x,y,color = COLOR))
    return ims

def InsertionSort(x,y,ims):
    for i in range(0,N):
        for j in range(i-1,1,-1):
            if y[j-1] > y[j]:
                y[i],y[j] = y[j],y[i]
                ims.appned(plt.bar(x,y,color = COLOR))
    return ims 

fig = plt.figure()
ims = []
x = [i+1 for i in range(N)]
y = [random.randint(VALUEMIN,VALUEMAX) for i in range(N)]
ims.append(plt.bar(x,y,color=COLOR))

ims = InsertionSort(x,y,ims)


ani = animation.ArtistAnimation(fig, ims, interval = 100)
ani.save("InsertSortanimation.mp4", writer="ffmpeg",dpi=300) 
