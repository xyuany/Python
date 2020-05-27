# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:09:18 2020

@author: yyuan
"""

'''
单项循环链表(Linked List)

单向循环链表的操作
·is_empty() 链表是否为空
·length() 链表长度
·travel() 遍历整个链表
·add(item) 链表头部添加元素
·append(item) 链表尾部添加元素
·insert(pos, item) 指定位置添加元素
·remove(item) 删除节点
·search(item) 查找节点是否存在
'''
#构造节点
class Node():
    def __init__(self, elem):
        #数据区
        self.elem = elem
        #节点地址指向，最开始为空
        self.next = None

#定义单链表
class SingleCircleLinkList():
    """单项循环链表"""
    #必须有一个类指针，指向头结点，用来连接整个单链表，属于对象属性
    def __init__(self, node = None):
        #单链表自己维护，使用单链表的用户不需要知道头结点的地址，作为私有属性。
        #新建单链表时，head可为空，或已经构造头结点，传入头结点，head指向头结点
        self.__head = node
        #判断头是否构造一个空的单向循环链表
        if node:
            node.next = node
            
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None
    
    def length(self):
        """链表长度"""
        #cursor游标，遍历节点
        cursor = self.__head
        #count记录数量
        #判断链表是否为空
        if self.is_empty():
            return 0
        else:
            count = 1
            while cursor.next !=self.__head:
                count +=1
                cursor = cursor.next
            return count
            
    
    def travel(self):
        """遍历整个链表"""
        cursor = self.__head
        #空链表没有cursor.next，判断是否为空链表
        if self.is_empty():
            return
        else:
            while cursor.next != self.__head:
                print(cursor.elem,end = ' ')
                cursor = cursor.next
            print(cursor.elem)

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        
        node.next = self.__head
        cursor = self.__head
        #判断是否为空链表
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cursor.next != self.__head:
                cursor = cursor.next
            cursor.next = node
            self.__head = node
    
    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        #头结点为空
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cursor = self.__head
            while cursor.next != self.__head:
                cursor = cursor.next
            cursor.next = node
            node.next = self.__head
        
    def insert(self, pos, item):
        """指定位置添加元素
        :param pos from 0
        """
        
        node = Node(item)
        
        count = 0
        cursor = self.__head
        
        if pos<=0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while count < pos-1:
                cursor = cursor.next
                count +=1
            node.next = cursor.next
            cursor.next = node
        
    
    def remove(self,item):
        """删除节点"""
        
        cursor = self.__head
        pre = None
        #判断是否为空链表
        if self.is_empty():
            return
        else:
            while cursor.next != self.__head:
                if cursor.elem == item:
                    #判断此节点是否是头结点，若是头结点
                    if cursor == self.__head:
                            #找到尾结点
                        while cursor.next != self.__head:
                            cursor=cursor.next
                        #删除头结点
                        cursor.next = self.__head.next
                        self.__head = cursor.next
                    #此节点为中间结点
                    else:
                        pre.next = cursor.next
                    return
                else:
                    pre = cursor
                    cursor = cursor.next
            #判断尾结点是否是被删除项
            if cursor.elem == item:
                #判断此尾结点是不是同为头结点，即此链表只有一个结点
                if self.length() ==1:
                    self.__head = None
                else:
                    pre.next = self.__head
            else:
                return
                
    
    
    def search(self,item):
        """查找节点是否存在"""
        cursor = self.__head
        if self.is_empty():
            return False
        else: 
            while cursor.next != self.__head:
                if cursor.elem == item:
                    return True
                else:
                    cursor = cursor.next
            if cursor.elem == item:
                    return True
            else:
                return False
    
if __name__ == "__main__":
    dll = SingleCircleLinkList()
    
    print(dll.is_empty())
    print(dll.length())
    
    dll.add(14)
    dll.append(15)
    print(dll.is_empty())
    print(dll.length())
    
    dll.append(16)
    dll.append(17)
    dll.append(18)
    dll.add(8)
    dll.append(19)
    dll.append(20)
    dll.append(21)
    dll.travel()
    dll.insert(4, "me")
    dll.travel()
