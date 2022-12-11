import random

class Individual:
    def updateFitness(self):
        #TODO implement fitness function
        sumfitness = 0
        for i in range(len(self.map.states)):#对于所有洲i
            for j in range(len(self.map.borders)):#对于所有边集j
                if self.map.borders[j].index1 == i:#当边j的起始index1为目前的洲时
                    if self.statescolor[i] != self.statescolor[self.map.borders[j].index2]:
                        #如果洲i的颜色与j边集中index2对应的洲的颜色不同时
                        sumfitness += 1#目标值？+1
        self.fitness = sumfitness#返回值（会有重复的吧 不会 因为index1和index2是区分开的

    def __init__(self,map):
        self.map=map
        self.fitness=0
        self.color=[0,1,2,3]
        self.statescolor=[]
        for i in range(len(map.states)):#洲i
            r=random.randint(0,3)#对每个州随机赋值
            self.statescolor.append(self.color[r])#每个州的颜色加入到statescolor中
        #TODO implement random generation of an individual
        self.updateFitness()

    def reproduce(self,x, y):#繁殖复制函数
        child1 = Individual(x.map)#个体x的图
        # TODO reproduce child from individuals x and y
        r = random.uniform(0,len(x.statescolor))#在0和长度之间生成一个实数r
        for i in range(len(x.statescolor)):#对于每个州
            if i < r:#如果这个洲小于实数
                child1.statescolor[i]=x.statescolor[i]#子代该洲颜色为x该洲的颜色
            else:#如果这个洲大于实数
                child1.statescolor[i]=y.statescolor[i]#子代该洲颜色为y该洲的颜色
        child1.updateFitness()#计算目标得分
        child2 = Individual(x.map)#再来一次？
        for i in range(len(x.statescolor)):
            if i > r:
                child2.statescolor[i]=x.statescolor[i]
            else:
                child2.statescolor[i]=y.statescolor[i]
        child2.updateFitness()
        if child1.fitness>child2.fitness:#看哪个子代好
            return child1
        else:
            return child2

    def mutate(self):#变异
        # TODO implement random mutation of the individual
        r = random.randint(0,len(self.statescolor)-1)#r为0-洲减1
        c = random.randint(0,3)#变化的颜色
        self.statescolor[r] = c#变化这个洲的颜色
        self.updateFitness()

    def isGoal(self):#是目标了吗
        print("fitness: " , self.fitness , " goalfitness: " , len(self.map.borders))#所有紧邻数
        return self.fitness == len(self.map.borders)

    def print(self):
        print("fitness: " , self.fitness)
        for i in range(len(self.statescolor)):
            print(self.map.states[i] , ": " , self.statescolor[i])
        print("0, 1, 2, and 3 represent 4 colors respectively.")