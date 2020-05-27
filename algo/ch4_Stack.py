# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:10:43 2020

@author: yyuan
"""

"""
栈(Stack)

Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数

顺序表list用尾部储存，链表从头部储存时间复杂度最低
"""

class Stack():
    """Stack"""
    def __init__(self):
        self.__list = []
        
    def push(self,item):
        """Add a new element item to Stack"""
        self.__list.append(item)
    
    def pop(self):
        """Pop the top element in Stack"""
        
        return self.__list.pop()
    
    def peak(self):
        """Return the top element of Stack"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        """Return if the Stack is empty"""
        return self.__list == []
    def size(self):
        """Return the size of the Stack"""
        return len(self.__list)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.pop()
