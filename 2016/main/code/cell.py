import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation
import random
import math
import map_da

class Car(object):
    def __init__(self, acc, pos, vector, max_vec, length, face):
        self.vector = vector
        self.acc = acc
        self.length = length
        self.pos = pos
        self.face = face
        self.max_vec = max_vec

    def turn_left(self):
        if self.face < 3:
            self.face += 1
        else:
            self.face = 0

    def turn_right(self):
        if self.face > 0:
            self.face -= 1
        else:
            self.face = 3

    def drive(self):
        if self.vector < self.max_vec:
            self.vector += self.acc
        else:
            self.vector = self.max_vec

    def stop(self):
        self.vector = 0

class Map(object):
    def __init__(self, car_num, map_data):
        self.car_num = car_num
        self.map_data = map_data
        self.cars = []

    def init(self):
        for i in range(self.car_num):
            self.cars.append(Car(0.1,[0,0],30,70,3,0))

    def run(self):
        for i in range(self.car_num):
            self.cars[i].drive()

    def plot(self):
        fig = plt.figure(figsize=(7,7))
        d, = plt.plot(self.cars[0].pos[0], self.cars[0].pos[1], 'bo')
        animation = FuncAnimation(fig, self.update, d, interval=10)
        plt.show()
    
    def update(self, dot, frame_number):
        self.cars[0].drive()
        self.cars[0].pos[0] += self.cars[0].vector

    def stop(self):
        pass

map1 = Map(50,map_da.map_data)
map1.init()
map1.run()
map1.plot()
