import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
xrange = np.arange(-3, 3, delta)
yrange = np.arange(-3, 3, delta)
X, Y = np.meshgrid(xrange,yrange)

#軸の設定
plt.axis([-4, 4, -4, 4])
plt.gca().set_aspect('equal', adjustable='box')

#描画
Z=X**2/4+Y**2/2-1
plt.contour(X, Y, Z, [0])
plt.show()