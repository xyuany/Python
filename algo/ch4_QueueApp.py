# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:35:11 2020

@author: yyuan
"""
"""
队列的应用
"""

from ch4_Queue import Queue
from ch4_Queue import Deque
import random

def hotPotato(namelist,num):
    """约瑟夫问题"""
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1 :
        #传递一轮
        #报数从1开始
        for i in range(1,num):
            simqueue.enqueue(simqueue.dequeue())
        #第num个出队
        simqueue.dequeue()
    
    return simqueue.dequeue()

"""
打印机问题抽象模型：
打印任务属性：提交时间，打印页数
打印队列：FIFO
打印机属性：打印速度，是否工作

生成概率：2pc/p/h, 10p in total = 3 min/pc -> 1/180
Page: 1~20

timer count: second per unit 

"""

class Printer:
    """printer类"""
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemining = 0
        
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemining -=1
            if self.timeRemining <= 0:
                self.currentTask = None
                
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemining = newtask.getPages()*60/self.pagerate
        
class Task():
    """task类"""
    def __init__(self,time):
        #生成时间戳
        self.timestamp = time
        #随机生成打印页数
        self.pages = random.randrange(1,21)
        
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    """生成task"""
    #以概率1/180 产生一个数，模拟生成任务概率
    num = random.randrange(1,181)
    if num==180:
        return True
    else:
        return False

def simulation(numSeconds, pagePerMinute):
    """模拟打印机"""
    labprinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitingtimes = []

    #模拟时间流逝
    for currentSecond in range(numSeconds):
        #如果生成newtask，加入队列
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        #如果打印机不忙并且队列不为空，则开始新的打印任务     
        if (not labprinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.dequeue()
            #记录等待时间
            waitingtimes.append(nexttask.waitTime(currentSecond))
            #打印机开始打印
            labprinter.startNext(nexttask)
        #时间流逝
        labprinter.tick()
    
    #计算等待时间
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))

"""
双端队列用例
"""
def palChecker(string):
    """回文数判断"""
    charDeque = Deque()
    
    for char in string:
        charDeque.add_rear(char)
    
    while charDeque.size() >1:
        if charDeque.remove_front() != charDeque.remove_rear():
            return False
    
    return True

    
if __name__ == '__main__':
    #print(hotPotato(range(1,50),7))
    #for i in range(10):
    #    simulation(3600, 5)
    print(palChecker('lsdkjfskf'))
    print(palChecker('rthejhjehtr'))
