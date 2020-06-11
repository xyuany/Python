# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:29:13 2020

@author: yyuan
"""

"""
堆Heap
"""

class BinHeap:
    """最小二叉堆"""
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def insert(self,key):
        self.heapList.append(key)
        self.currentSize +=1
        self.shiftUp(self.currentSize)
        
    def shiftUp(self, i):
        """上浮操作"""
        while i//2 >0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2]
            else:
                break
            i//=2
    def delMin(self):
        """删除最小值"""
        returnVal = self.heapList[1]
        # 头尾交换，pop尾
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -=1
        #新顶下沉
        self.shiftDown(1)
        return returnVal
    
    def shiftDown(self,i):
        """下沉操作"""
        
        #判断左子树在不在对内
        while (i *2) <= self.currentSize:
            # 找出左右节点更中更小节点的index，交换下沉
            minchild = self.minChild(i)
            if self.heapList[i] > self.heapList[minchild]:
                self.heapList[i],self.heapList[minchild] = self.heapList[minchild], self.heapList[i]
            i = minchild
    
    def minChild(self,i):
        #右节点index大于二叉堆总长，说明只有一个子节点
        if i*2+1 > self.currentSize:
            return i*2
        #左右节点都存在
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
    
    def buildHeap(self,alist):
        """无序列表生成堆"""
        self.heapList = [0] + alist
        self.currentSize = len(alist)
        
        # 最后一个节点的父节点开始下沉（叶节点无法下沉）
        i =  len(alist)//2
        print(len(self.heapList),i)
        while (i>0):
            print(self.heapList,i)
            self.shiftDown(i)
            i-=1
        print(self.heapList,i)
