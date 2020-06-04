# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:02:28 2020

@author: yyuan
"""
"""
栈的应用
"""
from ch4_Stack import Stack


def parChecker(string):
    """检查成对括号"""
    s = Stack()
    index = 0
    n = len(string)
    
    balance = True
    while index < n and balance is True:
        if string[index] in '([{':
            s.push(string[index])
        elif string[index] in ')]}':
            if s.is_empty():
                return False
            elif match(s.pop(),string[index]):
                balance = True
        else:
            return False
        index +=1

    if s.is_empty():
        return True
    else:
        return False

def match(left_par,right_par):
    left = '([{'
    right = ')]}'
    if left.index(left_par) == right.index(right_par):
        return True
    else:
        return False

def divideby2(number,n):
    s = Stack()
    while number >0:
        rem = number%n
        s.push(rem) 
        number = number//n
    result = ''
    while not s.is_empty():
        result += str(s.pop())
    return result
 
def infixToPostfix(infixexpr):
    """中缀表达式转为后缀表达式"""
    
    #优先级判断
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfixList.append(top)
                top = opStack.pop()
        else:
            #操作符比较
            while (not opStack.is_empty()) and (prec[token] <= prec[opStack.peak()]):
                postfixList.append(opStack.pop())                
            opStack.push(token)
        #print(postfixList)
        
    #读取完所有中缀表达式后，剩下栈内的操作符
    while not opStack.is_empty():
        postfixList.append(opStack.pop())
            
    return  ''.join(postfixList) 

def CalPostfix(postfixexpr):
    """计算后缀表达式"""
    operStack = Stack()
    tokenList = list(postfixexpr)
    
    for token in tokenList:
        if token in '0123456789':
            operStack.push(int(token))
        else:
            operand2 = operStack.pop()
            operand1 = operStack.pop()
            result = doMath(token,operand1,operand2)
            operStack.push(result)
    return operStack.pop()

def doMath(op,op1,op2):
    if op == '+':
        return op1+op2
    elif op == '-':
        return op1-op2
    elif op =='*':
        return op1*op2
    elif op == '/':
        return op1/op2


if __name__ == "__main__":
    #print(parChecker('(((())))'))
    #print(parChecker('((())'))
    #print(parChecker('(())))'))
    #print(divideby2(42))
    print(infixToPostfix('A + B * C + D'))
