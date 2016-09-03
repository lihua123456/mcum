from greedy import solve_tsp
import math
import numpy as np
import matplotlib.pyplot as plt
import pos_data

pos_list = pos_data.pos_list
D = []
T = []
X = [] 
Y = []
def get_list():
    tdm()
    for j in range(280):
        dis = []
        for i in range(280):
            if i==j:
                dis.append(9e9)
            else:
                dis.append((get_distance(pos_list[j],pos_list[i])-T[i]-T[j])*0.001)

        D.append(dis)

def get_distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def tdm():
    x_bar = reduce(lambda x,y:x+y, X)/280
    y_bar = reduce(lambda x,y:x+y, Y)/280
    dis = []
    for i in range(280):
        dis.append(get_distance([x_bar,y_bar],pos_list[i]))
    dis_bar = reduce(lambda x,y:x+y, dis)/280
    for i in range(280):
        T.append(get_distance([x_bar,y_bar],pos_list[i])-dis_bar)

def init():
    for i in range(280):
        X.append(pos_list[i][0])
        Y.append(pos_list[i][1])

def get_fit(path):
    fit = 0 #functools.reduce(get_distance,target)
    for i in range(280):
        dis = get_distance(pos_list[path[i]],pos_list[path[i+1]])
        # print('dis btw %d %d is %f'%(target[i],target[i+1],dis))
        fit = fit + dis
    return fit

init()
get_list()
path = pos_data.path_anti
p_31 = 0
for i in range(len(path)):
    if path[i] <= 30:
        path[i] -= 1
        p_31 = i
path.insert(p_31,30)
path.append(path[0])
print(get_fit(path))
plt.figure()
plt.plot(X[1:],Y[1:],'bo')
plt.plot(X[0],Y[0],'ro')
a = []
for i in range(280):
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
ax.quiver(px,py,u,v,color='b',angles='xy',scale_units='xy',scale=1)
plt.draw()
# plt.plot(px,py)
plt.show()
