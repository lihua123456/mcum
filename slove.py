#! /usr/bin/env python3
import random as rand
import numpy as np
import matplotlib.pyplot as plt
import functools
import pos_data

id_list = range(268)
pos_list=pos_data.pos_list
fitness=[]
group = []

def init():
    for i in range(1000):
        indev = []
        temp_list = list(range(268))
        for j in range(268):
            if j == 0:
                num = 1
            else:
                num = rand.choice(temp_list)
            indev.append(num)
            temp_list.remove(num)
        group.append(indev)

def mutate(indev):
    temp_list = list(range(268))
    p1 = rand.choice(temp_list)
    temp_list.remove(p1)
    p2 = rand.choice(temp_list)
    temp = indev[p2]
    indev[p2] = indev[p1]
    indev[p1] = temp
    return indev

def crossover(parent1,parent2):
    temp_length = list(range(20))
    temp_list = list(range(268))
    length =rand.choice(temp_length)
    pos = rand.choice(temp_list)
    seq = parent1[pos:pos+length]
    child = []
    while(i<268):
        if i == pos:
            child.extend(seq)
        if parent2[i] in seq:
            i = i+1
        else:
            child.append(parent2[i])
            i = i+1
    return child

def next_genration():
    for i in range(268):
        rete = np.random.rand(1)
        if rate[0] < 0.01:
            mutate(group[i])
        

def get_fit():
    for j in range(268):
        fit = 0 #functools.reduce(get_distance,target)
        for i in range(267):
            dis = get_distance(pos_list[group[j][i]],pos_list[group[j][i+1]])
            # print('dis btw %d %d is %f'%(target[i],target[i+1],dis))
            fit = fit + dis
        fitness.append(fit)
    fitness.sort()
    
def get_distance(p1,p2):
    return np.sqrt(np.power(p1[0]-p2[0],2)+np.power(p1[1]-p2[1],2))

init()
get_fit()
print(fitness)
