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
    for i in range(280):
        dis = get_distance(pos_list[path[i]],pos_list[path[i+1]])
        # print('dis btw %d %d is %f'%(target[i],target[i+1],dis))
        fit = fit + dis
    return fit

init()
get_list()
# path = solve_tsp(D,12)
path = [124, 141, 140, 125, 110, 94, 79, 80, 95, 111, 126, 139, 151, 168, 181, 182, 169, 152, 163, 153, 170, 183, 205, 211, 212, 213, 206, 244, 249, 250, 223, 224, 243, 202, 203, 194, 185, 193, 184, 172, 171, 155, 154, 143, 142, 123, 108, 91, 77, 61, 62, 76, 92, 107, 122, 118, 103, 86, 70, 73, 87, 104, 119, 136, 156, 173, 174, 157, 149, 166, 179, 186, 195, 191, 204, 200, 222, 227, 226, 225, 238, 239, 240, 241, 242, 253, 262, 263, 264, 265, 266, 254, 267, 268, 271, 270, 272, 269, 273, 274, 275, 255, 235, 236, 237, 230, 229, 228, 221, 220, 219, 218, 201, 192, 180, 167, 150, 138, 121, 117, 131, 148, 162, 176, 190, 199, 210, 217, 234, 245, 256, 276, 260, 251, 252, 261, 277, 257, 246, 231, 214, 207, 196, 189, 188, 197, 208, 215, 232, 247, 258, 278, 279, 259, 248, 233, 216, 209, 198, 187, 158, 165, 164, 175, 161, 147, 129, 134, 133, 114, 115, 116, 100, 84, 67, 72, 97, 96, 83, 99, 113, 128, 144, 145, 159, 177, 178, 160, 146, 127, 112, 98, 82, 81, 64, 48, 57, 49, 65, 71, 56, 41, 32, 23, 24, 25, 10, 11, 12, 9, 0, 1, 2, 3, 14, 4, 5, 6, 17, 16, 33, 42, 58, 75, 68, 53, 40, 27, 29, 30, 28, 15, 13, 26, 39, 50, 51, 52, 66, 54, 69, 85, 101, 106, 90, 89, 102, 132, 137, 130, 135, 120, 105, 88, 74, 59, 43, 35, 31, 7, 8, 18, 19, 34, 44, 60, 55, 45, 46, 36, 37, 20, 21, 22, 38, 47, 63, 78, 93, 109]
path.append(path[0])
print(get_fit(path))
print(path)
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
