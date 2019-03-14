"""
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
"""

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import  Axes3D
from matplotlib import cm
import math

# 定数
LIMIT = 1000 #反復回数の上限
N = 101 # x軸方向の分割数
M = 101 # y軸方向の分割数

def iteration(u):
    """
    １ステップ
    """
    u_next = [[0 for i in range(N)] for j in range(M)]
    diff = [[0 for i in range(N)] for j in range(M)]
    
    # 次のステップの値を計算
    for i in range(1,N-1):
        for j in range(1,M-1):
            u_next[i][j] = (u[i][j-1]+u[i-1][j]+u[i+1][j]+u[i][j+1])/4
    
    # # 1ステップ間の差(反復回数を決める参考)
    # for i in range(1,N-1):
    #     for j in range(1,M-1):
    #         diff[i][j]=u_next[i][j] - u[i][j]
    
    #値の更新
    for i in range(1,N-1):
        for j in range(1,N-1):
            u[i][j] = u_next[i][j]
    
    return diff

# 初期値
u = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    u[50][i] = math.sin(2*math.pi*i/(M-1)) # 初期値

# 計算
for i in range(LIMIT):
    iteration(u)

# 結果の出力
#diff = iteration(u)
#print(max([max(diff[i]) for i in range(N)])) #8.997129119334146e-05
#print(u)


# グラグの出力
x = np.arange(0,N)
y = np.arange(0,M)

X,Y = np.meshgrid(x,y)
fig = plt.figure()
ax = Axes3D(fig)
U = np.array(u)
ax.plot_wireframe(X,Y,U) # wireframe
#ax.plot_surface(X,Y,U,cmap=cm.coolwarm)
plt.show()