# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:27:15 2020

@author: yyuan
"""

"""
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小

dequeue > enqueue, 选择dequeue时间复杂度小的

双端队列(double-ended queue)

Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
"""

class Queue():
    def __init__(self):
        self.__list =[]
    
    def enqueue(self,item):
        self.__list.append(item)
    
    def dequeue(self):
        return self.__list.pop(0)
    
    def is_empty(self):
        return self.__list == []
    
    def size(self):
        return len(self.__list)

class Deque():
    def __init__(self):
        self.__list = []
        
    def add_front(self,item):
        self.__list.insert(0, item)
    
    def add_rear(self,item):
        self.__list.append(item)
    
    def remove_front(self):
        return self.__list.pop(0)
    
    def remove_rear(self):
        return self.__list.pop()
    def is_empty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    s.enqueue(6)
    s.enqueue(7)
    s.dequeue()
