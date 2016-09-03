# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random
import pos_data
import math
from GA import GA

class TSP(object):
    def __init__(self, aLifeCount = 100,):
        self.initCitys()
        self.lifeCount = aLifeCount
        self.ga = GA(aCrossRate = 0.8, 
            aMutationRage = 0.95, 
            aLifeCount = self.lifeCount, 
            aGeneLenght = len(self.citys)+1, 
            aMatchFun = self.matchFun())


    def initCitys(self):
        self.citys = pos_data.pos_list
        """
        for i in range(34):
              x = random.randint(0, 1000)
              y = random.randint(0, 1000)
              self.citys.append((x, y))
        """

          
    def distance(self, order):
        distance = 0.0
        for i in range(-1, len(self.citys) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

            """
            R = 6371.004
            Pi = math.pi 
            LatA = city1[1]
            LatB = city2[1]
            MLonA = city1[0]
            MLonB = city2[0]

            C = math.sin(LatA*Pi / 180) * math.sin(LatB * Pi / 180) + math.cos(LatA * Pi / 180) * math.cos(LatB * Pi / 180) * math.cos((MLonA - MLonB) * Pi / 180)
            D = R * math.acos(C) * Pi / 100
            distance += D
            """
        return distance


    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)


    def mainloop(self, n = 40000):
          while n > 0:
                self.ga.next()
                distance = self.distance(self.ga.best.gene)
                print (("%d : %f") % (n, distance))
                n -= 1
          return self.ga.best.gene

X = [] 
Y = []
pos_list = pos_data.pos_list
def main():
    tsp = TSP()
    path=tsp.mainloop()
    print(path)
    for i in range(280):
        X.append(pos_list[i][0])
        Y.append(pos_list[i][1])
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
    soa = np.array(a)
    px,py,u,v = zip(*soa)
    ax = plt.gca()
    ax.quiver(px,py,u,v,color='b',angles='xy',scale_units='xy',scale=1)
    plt.draw()
    plt.show()

if __name__ == '__main__':
      main()
