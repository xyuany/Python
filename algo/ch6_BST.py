# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:23:57 2020

@author: yyuan
"""

"""
BST(Binary Search Tree)
"""

class TreeNode:
    def __init__(self,key,val,left= None,right = None,parent = None):
        # 键值，数据项，左右子节点，父节点
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
        
    def hasLeftChild(self):
        return self.leftchild
    
    def hasRightChild(self):
        return self.rightchild
    
    def isLeftChild(self):
        """判断是不是父节点的左子节点"""
        return self.parent and self.parent.leftchild == self
    
    def isRightChild(self):
        """判断是否是父节点的右子节点"""
        return self.parent and self.parent.rightchild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.leftchild and self.rightchild)
    
    def hasAnyChildren(self):
        return self.rightchild or self.leftchild
    
    def hasBothChildren(self):
        return self.rightchild and self.leftchild
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.hasRightChild():
            self.rightchild.parent = self
    
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftchild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightchild:
                    yield elem

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size =0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
         """迭代器"""
         #用TreeNode类中重写的迭代器
         return self.root.__iter__()
    
    def put(self,key,value):
        """插入key构造BST"""
        #判断根节点
        if self.root:
            self._put(key,value,self.root)
        else:
            self.root = TreeNode(key, value)
        self.size +=1
    
    def _put(self,key,value,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,value,currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key, value,parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,value,currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key, value,parent = currentNode)
    
    def __setitem__(self,k,v):
        self.put(k, v)
        
    def get(self,key):
        """二叉查找树中找到节点key"""
        # 判断根节点
        if self.root:
            res = self._get(key,self.root)
            #判断递归查找是否找到
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def _get(self,key,currentNode):
        # 如果节点不存在，则返回空
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftchild)
        else:
            return self._get(key,currentNode.rightchild)
    
    def __getitem__(self,key):
        """根据key查找取值"""
        return self.get(key)
    
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    
    def delete(self,key):
        if self.size >1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -=1
            else:
                raise KeyError("Error, key not in the tree!")
        # 若key为根节点则将根节点清空
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -=1
        else:
            raise KeyError("Error, key not in the tree!")
    
    def __delitem__(self,key):
        return self.delete(key)
    
    def remove(self, currentNode):
        #叶子节点
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftchild:
                currentNode.parent.leftchild = None
            else:
                currentNode.parent.rightchild = None
        #被删除节点有两个子节点
        elif currentNode.hasBothChildren():
            # 找到后继项
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # 被删节点有一个子节点，则唯一子节点上移
        else:
            # 判断子节点是左子节点还是右子节点
            if currentNode.hasLeftChild():
                # 判断currentNode是否为父节点的左子节点
                if currentNode.isLeftChild():
                    currentNode.parent.leftchild = currentNode.leftchild
                    currentNode.leftchild.parent = currentNode.parent
                # currentNode为父节点的右子节点
                elif currentNode.isRightChild():
                    currentNode.parent.rightchild = currentNode.leftchild
                    currentNode.leftchild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.leftchild.key,currentNode.leftchild.payload,
                                                currentNode.leftchild.leftchild,
                                                currentNode.leftchild.rightchild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightchild
                elif currentNode.isRightChild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.rightchild
                else:
                    currentNode.replaceNodeData(currentNode.rightchild.key,
                                                currentNode.rightchild.payload,
                                                currentNode.rightchild.leftchild,
                                                currentNode.rightchild.rightchild)
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightchild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightchild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightchild = self
        return succ
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftchild
        return current
    
            
                    

if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3] = 'red' #__setitem__
    mytree[4] = 'blue'
    mytree[6] = 'yellow'
    mytree[2] = 'at'
    
    print(3 in mytree) #__contain__
    print(mytree[6]) #__getitem__
    
    print(mytree[2])
    for key in mytree:
        print(key,mytree[key])                
