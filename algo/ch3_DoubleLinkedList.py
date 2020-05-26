# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:07:00 2020

@author: yyuan
"""

'''
双向链表(Double Linked List)

双向链表的操作
·is_empty() 链表是否为空
·length() 链表长度
·travel() 遍历整个链表
·add(item) 链表头部添加元素
·append(item) 链表尾部添加元素
·insert(pos, item) 指定位置添加元素
·remove(item) 删除节点
·search(item) 查找节点是否存在
'''

class Node():
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None
        
class DoubleLinkList():
    """双链表"""
    def __init__(self,node = None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None
    
    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next
        print("")
        
    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        #考虑空链表
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node
    
    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        #判断是否为头结点
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
        
    def insert(self, pos, item):
        """指定位置添加元素
        :param pos from 0
        """
        if pos <=0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                count +=1
                cur = cur.next
            node.next = cur
            node.prev =cur.prev
            cur.prev = node
            node.prev.next = node
        
    
    def remove(self,item):
        """删除节点"""
        cur = self.__head
        
        while cur != None:
            if cur.elem == item:
                #判断是否为头结点
                if cur == self.__head:
                    self.__head = cur.next
                    cur.next.prev = None
                #判断是否为尾结点
                elif cur.next == None:
                    cur.prev.next = None
                #其余中间结点    
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
        
    
    
    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
    
if __name__ == "__main__":
    dll = DoubleLinkList()
    
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
