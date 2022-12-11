import random
from Border import Border
from Individual import Individual
from Map import Map
from Population import Population
import random
from Border import Border
from Individual import Individual
from map import map
from Population import Population

import networkx as nx
import matplotlib.pyplot as plt
import draw as draw
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon  # 上色
import time

def initMap(map):
    # 小胡的地图
    map.states.append("河北省")  # 0
    map.borders.append(Border(0, 1))#山东
    map.borders.append(Border(0, 10))#辽宁
    map.borders.append(Border(0, 11))#北京
    map.borders.append(Border(0, 12))#天津
    map.borders.append(Border(0, 23))#内蒙古
    map.borders.append(Border(0, 29))#山西
    map.borders.append(Border(0, 30))#河南
    map.states.append("山东省")  # 1
    map.borders.append(Border(1, 3))#江苏
    map.borders.append(Border(1, 30))#河南
    map.borders.append(Border(1, 2))#安徽
    map.states.append("安徽省")  # 2
    map.borders.append(Border(2, 3))#江苏
    map.borders.append(Border(2, 5))#浙江
    map.borders.append(Border(2, 6))#江西
    map.borders.append(Border(2, 31))#湖北
    map.borders.append(Border(2, 30))#河南
    map.states.append("江苏省")  # 3
    map.borders.append(Border(3, 4))#上海
    map.borders.append(Border(3, 5))#浙江
    map.states.append("上海市")  # 4
    map.borders.append(Border(4, 5))#浙江
    map.states.append("浙江省")  # 5
    map.borders.append(Border(5, 6))#江西
    map.borders.append(Border(5, 7))#福建
    map.states.append("江西省")  # 6
    map.borders.append(Border(6, 7))#福建
    map.borders.append(Border(6, 31))#湖北
    map.borders.append(Border(6, 32))#湖南
    map.borders.append(Border(6, 33))#广东
    map.states.append("福建省")  # 7
    map.borders.append(Border(7, 33))#广东
    map.states.append("黑龙江省")  # 8
    map.borders.append(Border(8, 9))#吉林
    map.borders.append(Border(8, 23))#内蒙古
    map.states.append("吉林省")  # 9
    map.borders.append(Border(9, 23))#内蒙古
    map.borders.append(Border(9, 10))#辽宁
    map.states.append("辽宁省")  # 10
    map.borders.append(Border(10, 23))#内蒙古
    map.states.append("北京市")  # 11
    map.borders.append(Border(11, 12))#天津
    map.states.append("天津市")  # 12

    map.states.append("海南省")  # 13

    map.states.append("台湾省")  # 14

    map.states.append("澳门特别行政区")  # 15

    map.states.append("香港特别行政区")  # 16

    map.states.append("新疆维吾尔自治区")  # 17
    map.borders.append(Border(17, 18))#西藏
    map.borders.append(Border(17, 19))#青海
    map.borders.append(Border(17, 20))#甘肃
    map.states.append("西藏自治区")  # 18
    map.borders.append(Border(18, 19))#青海
    map.borders.append(Border(18, 21))#四川
    map.borders.append(Border(18, 22))#云南
    map.states.append("青海省")  # 19
    map.borders.append(Border(19, 20))#甘肃
    map.borders.append(Border(19, 21))#四川
    map.states.append("甘肃省")  # 20
    map.borders.append(Border(20, 21))#四川
    map.borders.append(Border(20, 23))#内蒙古
    map.borders.append(Border(20, 24))#宁夏
    map.borders.append(Border(20, 25))#陕西
    map.states.append("四川省")  # 21
    map.borders.append(Border(21, 22))#云南
    map.borders.append(Border(21, 25))#陕西
    map.borders.append(Border(21, 26))#重庆
    map.borders.append(Border(21, 27))#贵州
    map.states.append("云南省")  # 22
    map.borders.append(Border(22, 28))#广西
    map.borders.append(Border(22, 27))#贵州
    map.states.append("内蒙古自治区")  # 23
    map.borders.append(Border(23, 29))#山西
    map.borders.append(Border(23, 24))#宁夏
    map.borders.append(Border(23, 25))#陕西
    map.states.append("宁夏回族自治区")  # 24
    map.borders.append(Border(24, 25))#陕西
    map.states.append("陕西省")  # 25
    map.borders.append(Border(25, 30))#河南
    map.borders.append(Border(25, 31))#湖北
    map.borders.append(Border(25, 29))#山西
    map.borders.append(Border(25, 26))#重庆
    map.states.append("重庆市")  # 26
    map.borders.append(Border(26, 31))#湖北
    map.borders.append(Border(26, 32))#湖南
    map.borders.append(Border(26, 27))#贵州
    map.states.append("贵州省")  # 27
    map.borders.append(Border(27, 28))#广西
    map.borders.append(Border(27, 32))#湖南
    map.states.append("广西壮族自治区")  # 28
    map.borders.append(Border(28, 32))#湖南
    map.borders.append(Border(28, 33))#广东
    map.states.append("山西省")  # 29
    map.borders.append(Border(29, 30))#河南
    map.states.append("河南省")  # 30
    map.borders.append(Border(30, 31))#湖北
    map.states.append("湖北省")  # 31
    map.borders.append(Border(31, 32))#湖南
    map.states.append("湖南省")  # 32
    map.borders.append(Border(32, 33))#广东
    map.states.append("广东省")  # 33


if __name__ == '__main__':
    map = Map()
    initMap(map) #以目前的地图进行初始化
    populationSize = 100 # TODO find reasonable value 种群规模
    population = Population(map, populationSize) #按规模生成一个种群population，都是随机赋值的地图

    maxIterations = 500 # TODO find reasonable value #最大迭代次数
    currentIteration = 0 #目前是0
    goalFound = False #是否达成目标
    bestIndividual = Individual(map) # to hold the individual representing the goal, if any 最好的个体 现在是随机赋值的map
    mark = 0 #标记为0
    while currentIteration < maxIterations and goalFound==False: #如果现在的迭代次数小于最大值，并且没有达到目标
        newPopulation = Population(map,0)#新的种群 生成一个规模为0的？
        bestparent=Individual(map)#bestparent为随机赋值地图
        worstchild=Individual(map)#worstchild为随机赋值地图
        #对于单次迭代！
        for i in range(populationSize):#对于一个种群规模内的所有个体i，所以这个i是生成的子代个数才对
            x,y= population.randomSelection()#x，y是种群中按概率随机选择的两个个体
            if x.fitness>y.fitness :#如果x的目标值>y
                if bestparent.fitness<x.fitness:#如果x>bestparent的目标值
                    bestparent=x#bestparent变为x
            else:
                if bestparent.fitness < y.fitness:#如果y>bestparent的目标值
                    bestparent = y#bestparent变为y
            child = Individual.reproduce(x, x, y)#self是x，x，y作为父母进行繁殖，得到一个相对优秀的孩子
            pmutate=random.random()#变异概率
            if pmutate < 0.3 :# TODO use small probability instead如果<0.3，那么发生变异
                child.mutate()
            if child.isGoal():#如果这个孩子达成目标，退出循环，最好个体变为该孩子
                goalFound = True
                bestIndividual = child
                mark=1
                break
            newPopulation.vector.append(child)#新的种群里加上孩子，该种群的初始为0
        currentIteration += 1#迭代次数加一
        if mark == 1:
            break

        worstmark=0
        for i in range(len(newPopulation.vector)):#对于由孩子所组成的新种群，其中的每一个孩子i
            if newPopulation.vector[i].fitness<worstchild.fitness:#如果i的目标值小于最差的孩子的目标值
                worstchild=newPopulation.vector[i]#最差的孩子变为当前这个
                worstmark=i#最差的标记为i
        newPopulation.vector[worstmark]=bestparent#那么新种群的这个最差的，让它变成bestparent
        population = newPopulation#种群变为新种群


    if goalFound :
        print("Found a solution after ",currentIteration," iterations" )
        bestIndividual.print()
        G = nx.Graph()
        labels={}
        for i in range(len(map.states)):
            G.add_node(i)
            labels[i]=map.states[i]
        for i in range(len(map.borders)):
            G.add_edge(map.borders[i].index1,map.borders[i].index2)
        pos = nx.spring_layout(G)
        colors = bestIndividual.statescolor
        nx.draw_networkx_nodes(G, pos, node_color=colors)
        nx.draw_networkx_labels(G,pos,labels)
        nx.draw_networkx_edges(G, pos)
        plt.axis('off')
        plt.show()

        cnMap = draw.ChinaMap()  #Initialization
        print(cnMap.getProvinceName(0))

        newListindex=[]
        for i in range(len(map.states)):
            newListindex.append((cnMap.nameList.tolist().index(map.states[i])))
            
        print(map.states[i],newListindex)
        

        for i in range(len(map.states)):
            cnMap.changeColor(cnMap.nameList.tolist().index(map.states[i]),bestIndividual.statescolor[i])

        cnMap.draw(newListindex)
        cnMap.stop()

        # 画中国地图
        m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
        m.readshapefile('shapefiles/china', 'china', drawbounds=True)

        # 得到中国的各个省，使用set不会重复
        locatName = set()
        for i in m.china_info:
            name = i['OWNER']
            locatName.add(name.replace("\x00", ""))

        # 将set转换为list方便处理
        nameList = list(locatName)
        print(nameList)
        print(len(nameList))

        # 初始化每个省的颜色为0
        nameDict = dict()
        for i in nameList:
            nameDict[i] = 0
        print(nameDict)
        print(len(nameDict))


        # 得到 s 省相邻地区的颜色列表
        def getColorList(s):
            colorList = []
            for i in str[s]:
                colorList.append(nameDict[i])
            return colorList


        #  给 seg 地区 画 k 颜色
        ax = plt.gca()


        def pColor(seg, k):
            colorStr = ""
            if k == 1:
                colorStr = "r"
            elif k == 2:
                colorStr = "y"
            elif k == 3:
                colorStr = "b"
            elif k == 4:
                colorStr = "g"
            elif k == 5:
                colorStr = "pink"
            poly = Polygon(seg, facecolor=colorStr)  # r, y, b, g, pink
            ax.add_patch(poly)
            ###############################
            # 开始上色
            name = ""
            colorList = []
            c = 0
            for seg, mName in zip(m.china, m.china_info):
                ttName = mName['OWNER']
                tName = ttName.replace("\x00", "")
                if tName != name:
                    colorList = getColorList(tName)
                    for i in range(1, 6):  # 从低到高上色
                            if i not in colorList:  # 不存在就上色
                                    c = i
                                    break
                pColor(seg, c)
                nameDict[tName] = c
                name = tName
                plt.show()
    else:
        print("Did not find a solution after ",currentIteration," iterations")
        print("Please run it again...")