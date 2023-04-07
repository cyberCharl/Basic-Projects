import matplotlib.pyplot as plt 
import numpy as np 
import sys

sys.setrecursionlimit(10000)

plt.style.use('_mpl-gallery')

x = np.empty(10000, dtype=float) 
y = np.empty(10000, dtype=float)

def tinkerbell(x, y, n, xArr, yArr):
    if (n == 5000):
        return [x,y]
    new_x = x**2 - y**2 + .9*x - .6*y
    new_y = 2*x*y + 2*x + .5*y
    n+=1
    xArr.put(n, new_x)
    yArr.put(n, new_y)
    return tinkerbell(new_x, new_y, n,xArr,yArr)

if __name__ == "__main__":
    tinkerbell(-0.7,-0.6, 0, x, y)
    plt.scatter(x,y)
    plt.show()
