
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:18:12 2020

@author: yyuan
"""

'''
链表(Linked List)

单链表的操作
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
class SingleLinkList():
    #必须有一个类指针，指向头结点，用来连接整个单链表，属于对象属性
    def __init__(self, node = None):
        #单链表自己维护，使用单链表的用户不需要知道头结点的地址，作为私有属性。
        #新建单链表时，head可为空，或已经构造头结点，传入头结点，head指向头结点
        self.__head = node
    
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None
    
    def length(self):
        """链表长度"""
        #cursor游标，遍历节点
        cursor = self.__head
        #count记录数量
        count = 0
        while cursor !=None:
            count +=1
            cursor = cursor.next
        return count
            
    
    def travel(self):
        """遍历整个链表"""
        cursor = self.__head
        while cursor != None:
            print(cursor.elem,end = ' ')
            cursor = cursor.next
        print("")
        
    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
    
    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        #头结点为空
        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = node
        
    def insert(self, pos, item):
        """指定位置添加元素
        :param pos from 0
        """
        
        node = Node(item)
        
        count = 0
        cursor = self.__head
        
        if pos<0:
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
        
        while cursor != None:
            if cursor.elem == item:
                #判断此节点是否是头结点，若是头结点
                if cursor == self.__head:
                    self.__head = cursor.next
                else:
                    pre.next = cursor.next
                break
            else:
                pre = cursor
                cursor = cursor.next
    
    
    def search(self,item):
        """查找节点是否存在"""
        cursor = self.__head
        while cursor != None:
            if cursor.elem == item:
                return True
            else:
                cursor = cursor.next
        return False
    
if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(15)
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(16)
    ll.append(17)
    ll.append(18)
    ll.add(8)
    ll.append(19)
    ll.append(20)
    ll.append(21)
    ll.insert(4, "me")
    ll.travel()
    ll.search(19)
