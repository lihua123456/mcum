from greedy import solve_tsp
import math
import numpy as np
import matplotlib.pyplot as plt
import pos_data

pos_list = pos_data.pos_list
D = []
X = [] 
Y = []
def get_list():
    for j in range(280):
        dis = []
        for i in range(280):
            dis.append(get_distance(pos_list[j],pos_list[i]))
        D.append(dis)

def get_distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def init():
    for i in range(280):
        X.append(pos_list[i][0])
        Y.append(pos_list[i][1])

def get_fit(path):
    fit = 0 #functools.reduce(get_distance,target)
    for i in range(279):
        dis = get_distance(pos_list[path[i]],pos_list[path[i+1]])
        # print('dis btw %d %d is %f'%(target[i],target[i+1],dis))
        fit = fit + dis
    return fit

get_list()
init()
path = solve_tsp(D)
print(get_fit(path))
plt.figure()
plt.plot(X[1:],Y[1:],'bo')
plt.plot(X[0],Y[0],'ro')
a = []
for i in range(279):
    xp = X[path[i]]
    yp = Y[path[i]]
    xl = X[path[i+1]] - xp
    yl = Y[path[i+1]] - yp
    temp = [xp, yp, xl, yl]
    a.append(temp)

# plt.setp(lines, color='r', linewidth=2.0)
soa = np.array(a)
px,py,u,v = zip(*soa)
ax = plt.gca()
ax.quiver(px,py,u,v,angles='xy',scale_units='xy',scale=1)
plt.draw()
# plt.plot(px,py)
plt.show()
