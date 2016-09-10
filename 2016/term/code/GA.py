# -*- coding: utf-8 -*-

import random
import math
import pos_data
from Life import Life

pos_list=pos_data.pos_list

class GA(object):
    """遗传算法类"""
    def __init__(self, aCrossRate, aMutationRage, aLifeCount, aGeneLenght, aD, aMatchFun = lambda life : 1):
        self.croessRate = aCrossRate
        self.mutationRate = aMutationRage
        self.lifeCount = aLifeCount
        self.geneLenght = aGeneLenght
        self.matchFun = aMatchFun                 # 适配函数
        self.lives = []                           # 种群
        self.best = None                          # 保存这一代中最好的个体
        self.generation = 1
        self.D = aD
        self.crossCount = 0
        self.mutationCount = 0
        self.bounds = 0.0                         # 适配值之和，用于选择是计算概率

        dis_min = []
        for i in range(self.geneLenght):
            _temp = self.D[i][0]
            for j in range(self.geneLenght):
                if _temp > self.D[i][j]:
                    _temp = self.D[i][j]
                    temp = j
            dis_min.append(temp)
        self.Min = dis_min
        self.initPopulation()


    def initPopulation(self):
        """初始化种群"""
        path_solve = pos_data.path_solve
        path_greddy = pos_data.path_greddy
        self.lives = []
        for i in range(self.lifeCount):
            gene = [x for x in range(0,self.geneLenght)]
            # gene = []
            # rate =random.randint(1,100)
            # if rate > 55:
                # gene.extend(path_greddy)
            # else:
                # gene.extend(path_solve)

            # rate =random.randint(1,100)
            # if  rate > 50:
                # random.shuffle(gene)
            random.shuffle(gene)
            # gene.insert(0,0)
            # gene.append(0)
            life = Life(gene)
            self.lives.append(life)


    def judge(self):
        """评估，计算每一个个体的适配值"""
        self.bounds = 0.0
        self.best = self.lives[0]
        for life in self.lives:
            life.score = self.matchFun(life)
            self.bounds += life.score
            if self.best.score < life.score:
                self.best = life

    def get_distance(self,c1,c2):
        p1=pos_list[c1]
        p2=pos_list[c2]
        return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))
          
    def miner_one(self,index,lis):
        num = int(index)
        if num==0:
            num = len(lis) - 1
        else:
            num -= 1
        return num

    def plus_one(self,index,lis):
        num = int(index)
        if num==(len(lis) - 1):
            num = 0
        else:
            num += 1
        return num

    def cross(self, parent1, parent2):
        index = random.randint(0, self.geneLenght - 1)
        rp1,rp2=list(parent1.gene),list(parent2.gene)
        lp1,lp2=list(parent1.gene),list(parent2.gene)
        index2 = int(index)
        node = rp1[index]
        newGene1,newGene2 = [node],[node]
        rp1.remove(node)
        rp2.remove(node)
        lp1.remove(node)
        lp2.remove(node)
        while(len(rp1)>=1):
            temp_index = self.miner_one(index,rp1)
            d1 = self.D[rp1[temp_index]][node]
            d2 = self.D[rp2[temp_index]][node]
            if d1<d2:
                node = rp1[temp_index]
            else:
                node = rp2[temp_index]
            index = temp_index
            newGene1.append(node)
            rp1.remove(node)
            rp2.remove(node)
        while(len(lp1)>=1):
            temp_index = self.plus_one(index,lp1)
            d1 = self.D[lp1[temp_index]][node]
            d2 = self.D[lp2[temp_index]][node]
            if d1<d2:
                node = lp1[temp_index]
            else:
                node = lp2[temp_index]
            index2 = temp_index
            newGene2.append(node)
            lp1.remove(node)
            lp2.remove(node)
        self.crossCount += 1
        return newGene1,newGene2

    def cross_bk(self, parent1, parent2):
        """交叉"""
        index1 = random.randint(0, self.geneLenght - 1)
        index2 = random.randint(index1, self.geneLenght - 1)
        tempGene = parent2.gene[index1:index2]   # 交叉的基因片段
        newGene = []
        p1len = 0
        for g in parent1.gene:
            if p1len == index1:
                newGene.extend(tempGene)     # 插入基因片段
                p1len += 1
            if g not in tempGene:
                newGene.append(g)
                p1len += 1
        self.crossCount += 1
        return newGene

    def  mutation_bk(self, gene):
        index = random.randint(1, self.geneLenght - 1)
        min_to = self.Min[gene[index]]
        index2 = gene.index(min_to)
        if index < index2:
            part1 = gene[0:index+1]
            part2 = gene[index+1:index2+1][::-1]
            part2.reverse()
            part3 = gene[index2+1:]
        else:
            part1 = gene[0:index2]
            part2 = gene[index2:index][::-1]
            part3 = gene[index:]

        newGene = []
        newGene.extend(part1)
        newGene.extend(part2)
        newGene.extend(part3)
        self.mutationCount += 1

        return newGene

    def  mutation(self, gene):
          """突变"""
          index1 = random.randint(1, self.geneLenght - 2)
          index2 = random.randint(1, self.geneLenght - 2)

          newGene = gene[:]       # 产生一个新的基因序列，以免变异的时候影响父种群
          newGene[index1], newGene[index2] = newGene[index2], newGene[index1]
          self.mutationCount += 1
          return newGene


    def getOne(self):
          """选择一个个体"""
          r = random.uniform(0, self.bounds)
          for life in self.lives:
                r -= life.score
                if r <= 0:
                      return life

          raise Exception("选择错误", self.bounds)


    def newChild(self):
        """产生新后的"""
        parent1 = self.getOne()
        parent2 = self.getOne()
        rate = random.random()

        # 按概率交叉
        if rate < self.croessRate:
            # 交叉
            gene1,gene2 = self.cross(parent1, parent2)
        else:
            gene1,gene2 = parent1.gene,parent2.gene

        # 按概率突变
        rate = random.random()
        if rate < self.mutationRate:
            gene1,gene2 = self.mutation(gene1),self.mutation_bk(gene2)

        return Life(gene1),Life(gene2)


    def next(self):
        """产生下一代"""
        self.judge()
        newLives = []
        newLives.append(self.best)            #把最好的个体加入下一代
        while len(newLives) < self.lifeCount-1:
            child1,child2=self.newChild()
            newLives.append(child1)
            newLives.append(child2)
        if len(newLives) < self.lifeCount:
            newLives.append(child1)
        self.lives = newLives
        self.generation += 1
		
