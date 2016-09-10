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
                # dis.append(get_distance(pos_list[j],pos_list[i]))

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
    for i in range(279):
        dis = get_distance(pos_list[path[i]],pos_list[path[i+1]])
        # print('dis btw %d %d is %f'%(target[i],target[i+1],dis))
        fit = fit + dis
    return fit

init()
get_list()
# path = solve_tsp(D,12)
path= [ 40, 27, 14, 3, 2, 1, 0, 9, 12, 11, 10, 25, 24, 23, 32, 41, 56, 49, 57, 48, 64, 81, 82, 98, 112, 127, 146, 160, 159, 178, 177, 187, 198, 197, 188, 164, 165, 158, 145, 144, 128, 133, 134, 115, 114, 113, 99, 96, 83, 65, 71, 72, 67, 84, 97, 100, 116, 129, 147, 161, 175, 189, 196, 207, 214, 231, 215, 208, 209, 216, 233, 232, 247, 248, 259, 279, 278, 258, 246, 257, 277, 261, 252, 251, 260, 276, 256, 245, 234, 217, 210, 199, 190, 176, 162, 148, 131, 117, 101, 85, 75, 90, 106, 89, 102, 137, 132, 121, 138, 150, 167, 180, 192, 201, 218, 219, 220, 221, 228, 229, 230, 237, 236, 235, 255, 275, 274, 273, 269, 272, 270, 271, 268, 254, 267, 266, 265, 264, 253, 263, 262, 250, 249, 223, 211, 212, 213, 244, 206, 181, 182, 169, 168, 151, 139, 126, 125, 140, 152, 163, 183, 205, 224, 243, 242, 241, 240, 239, 238, 225, 226, 227, 222, 200, 204, 195, 191, 179, 186, 166, 174, 156, 173, 185, 194, 203, 202, 193, 184, 172, 154, 143, 142, 155, 171, 170, 153, 141, 124, 109, 93, 94, 110, 111, 95, 80, 79, 78, 63, 47, 38, 22, 36, 21, 20, 37, 45, 62, 46, 61, 77, 76, 92, 91, 108, 123, 122, 107, 118, 103, 86, 70, 55, 60, 73, 87, 104, 119, 136, 157, 149, 135, 130, 120, 105, 88, 74, 59, 43, 44, 34, 19, 18, 35, 31, 8, 7, 6, 5, 4, 16, 17, 33, 42, 58, 53, 68, 69, 54, 52, 66, 51, 50, 39, 26, 13, 15, 28, 30, 29]
# path.append(path[0])
print(get_fit(path))
# print(path)
plt.figure()
plt.plot(X,Y,'bo')
plt.plot(X[40],Y[40],'ro')
plt.plot(X[29],Y[29],'go')
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
ax.quiver(px,py,u,v,color='b',angles='xy',scale_units='xy',scale=1)
plt.draw()
# plt.plot(px,py)
plt.show()
