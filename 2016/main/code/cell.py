import numpy as np
import matplotlib.pyplot as plt
import getopt,sys
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
        self.length = len(map_data[0])
        self.width = len(map_data)
        self.cars = []

    def init(self):
        for i in range(self.car_num):
            self.cars.append(Car(0.1,[0,0],3,7,1,0))

    def run(self):
        for i in range(self.car_num):
            self.cars[i].drive()

    def plot(self):
        from PIL import Image, ImageDraw
        img = Image.new("RGB",(self.length*5,self.width*5),(0,0,0))
        draw = ImageDraw.Draw(img)
    
        for y in range(self.length):
            for x in range(self.width):
                if self.map_data[x][y]==0: draw.rectangle((y*5,x*5,y*5+5,x*5+5),(255,255,255))
        img.show() 

 
    def stop(self):
        pass

map1 = Map(50,map_da.map_data)
map1.init()
map1.run()
map1.plot()
