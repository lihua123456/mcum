from tsp_solver.greedy import solve_tsp
import math
import matplotlib.pyplot as plt
import pos_data

pos_list = pos_data.pos_list
D = []
X = [] 
Y = []
def get_list():
    for j in range(268):
        dis = []
        for i in range(268):
            dis.append(get_distance(pos_list[j],pos_list[i]))
        D.append(dis)

def get_distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def init():
    for i in range(268):
        X.append(pos_list[i][0])
        Y.append(pos_list[i][1])

get_list()
init()
path = solve_tsp( D )

plt.plot(X,Y,'bo')
px = []
py = []
for i in range(268):
    px.append(X[path[i]])
    py.append(Y[path[i]])
# plt.setp(lines, color='r', linewidth=2.0)
plt.plot(px,py)
plt.show()
