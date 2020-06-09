# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:41:51 2020

@author: yyuan
"""

def listsum(numList):
    if len(numList) ==1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
    
def digitConvert(integer,base):
    convString = '0123456789ABCDEF'
    if integer < base:
        return convString[integer]
    else:
        return digitConvert(integer//base, base)+ convString[integer%base]

#%% Sierpinski Draw
import turtle

#绘制谢尔宾斯基三角形
def sierpinski(degree,points):
    colormap = ['blue','red','green','white','yellow','orange']
    drawTriangle(points,colormap[degree])
    if degree > 0:
        #按照左上右顺序画图
        sierpinski(degree-1, {'left':points['left'],
                              'top':getMid(points['left'],points['top']),
                              'right':getMid(points['left'],points['right'])})
        
        sierpinski(degree-1, {'left':getMid(points['left'],points['top']),
                              'top':points['top'],
                              'right':getMid(points['top'],points['right'])})
        
        sierpinski(degree-1, {'left':getMid(points['left'],points['right']),
                              'top':getMid(points['top'],points['right']),
                              'right':points['right']})

def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def getMid(p1,p2):
    return (p1[0]+p2[0])/2,(p1[1]+p2[1])/2


t = turtle.Turtle()
points = {'left':(-200,-100),
          'top':(0,200),
          'right':(200,-100)}
sierpinski(5, points)
turtle.done()

#%% Hannoi Tower
def moveTower(height,fromPole,withPole,toPole):
    if height >=1:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height-1,withPole,fromPole,toPole)

def moveDisk(disk,fromPole,toPole):
    print(f'Moving disk[{disk}] from {fromPole} to {toPole}')

moveTower(3, '#1','#2','#3')

#%% ReceiveMoney_recursion
def recMC(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins <minCoins:
                minCoins = numCoins
    return minCoins


def recDC(coinValueList,change,knownResults):
    minCoins = change
    #递归条件结束
    if change in coinValueList:
        #记录最优解
        knownResults[change] = 1
        return 1
    #查表成功，使用最优解
    elif knownResults[change] >0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <=change]:
            numCoins = 1+ recDC(coinValueList, change - i, knownResults)
            
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

#%% ReceiveMoney_DynamicProg
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    #从1分开始到change逐个计算最少的硬币数
    for cents in range(1,change+1):
        #初始化最大值
        coinCount = cents
        #初始化新加硬币
        newCoin = 1
        #减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1 < coinCount:
                coinCount = minCoins[cents-j]+1
                #记录硬币面值
                newCoin = j
        #得到当前最小的硬币书，记录在表
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
        print(cents,coinCount)
    
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin-thisCoin

amnt = 63
clist = [1,5,10,21,25]
coinsUsed = [0] *(amnt + 1)
coinCount = [0] *(amnt + 1)

print("Making change for",amnt, 'requires')
print(dpMakeChange(clist, amnt, coinCount, coinsUsed),"coins")
print("They are:")
printCoins(coinsUsed, amnt)
print("The used list is as follows:")
print(coinsUsed)

#%% 最大背包问题

#解法没有考虑所有只能用1次
def maxValue(maxVolumn,weightList,valueList,maxValueList):
    #根据重量，循环得到每个重量的最大value
    for volumn in range(1,maxVolumn+1):
        #设置value的最大值为一个较小的数
        maxValue = 0
        #得到可以使用的宝物的item,则可得到相应的重量及价值
        for i in [item for item in range(len(weightList)) if weightList[item]<=volumn]:
            #比较价值
            if maxValueList[volumn-weightList[i]]+valueList[i] > maxValue:
                maxValue = maxValueList[volumn-weightList[i]]+valueList[i]
        
        maxValueList[volumn] = maxValue
    
    return maxValueList

maxVolumn = 20 
weightList = [2,3,4,5,9]
valueList = [3,4,8,8,10]
maxValueList = [0] * (maxVolumn +1)

print(maxValue(maxVolumn, weightList, valueList, maxValueList))

#%%

tr = [None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
max_w = 20

#初始化表格m[(item,weight)]
#表示在前i个宝物中，与最大重量w的组合，所得到的最大价值
#当i什么都不取，或者w为0，价值均为0

m = {(i,w):0 for i in range(len(tr)) for w in range(max_w+1)}

#逐个填写表格
for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]['w'] > w: #无法装下宝物i
            m[(i,w)] = m[(i-1,w)] #不装i，继承前一个value
        else:
            #装宝物与不装的最大值
            m[(i,w)] = max(m[(i-1,w)],m[(i-1, w-tr[i]['w'])]+tr[i]['v'])

print(m[(len(tr)-1,max_w)])
