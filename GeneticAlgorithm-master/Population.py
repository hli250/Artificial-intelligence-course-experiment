#Class representing a population of individuals
import random

from Individual import Individual

class Population:
    def __init__(self,map,initialSize):
        self.vector=[]
        for i in range(initialSize):#一个种群有多少个体
            self.vector.append(Individual(map))

    def randomSelection(self):#随机选择两个个体
        # TODO implement random selection
        # an individual should be selected with a probability
        # proportional to its fitness
        sumfiness=0
        for i in range(len(self.vector)):
            sumfiness+=self.vector[i].fitness
        fitness_list=[]
        for i in range(len(self.vector)):
            fitness_list.append(float(self.vector[i].fitness)/float(sumfiness))
        r=random.choices(self.vector,weights=fitness_list,k=2)#按种群的概率来选取！！！
        while r[0]==r[1] :
            r = random.choices(self.vector, weights=fitness_list, k=2)
        return r[0],r[1]