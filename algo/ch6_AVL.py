# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:11:58 2020

@author: yyuan
"""

"""
AVL: 平衡二叉查找树
"""

from ch6_BST import BinarySearchTree
from ch6_BST import TreeNode

class AVL(BinarySearchTree):
    def _put(self,key,value,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key, value)
                self.updateBalance(currentNode.leftchild)
        else:
            if currentNode.hasRightChild():
                self._put(key,value,currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key, value)
                self.updateBalance(currentNode.rightchild)
            
    def updateBalance(self,node):
        """平衡函数"""
        if node.balanceFactor >1 or node.balanceFactor <-1:
            self.rebalance(node)
            return
        
        #调节父节点
        if node.parent !=None:
            if node.isLeftChild():
                node.parent.balanceFactor +=1
            elif node.isRightChild():
                node.parent.balanceFactor -=1
        
            #调整父节点的平衡因子
            if node.parent.balanceFactor !=0:
                self.updateBalance(node.parent)
            
    #重新旋转
    def rebalance(self,node):
        #判断是否为右重
        if node.balanceFactor <0:
            #检查右重node的右子节点是否是左重，如果是，则先将左重的节点右旋，再将node左旋
            if node.rightchild.balanceFactor >0:
                self.singleRightRotate(node.rightchild)
                self.singleLeftRotate(node)
            else:
                #只需要左旋
                self.singleLeftRotate(node)
        elif node.balanceFactor >0:
            #检查左重的node的左子节点是否为右重
            if node.leftchild.balanceFactor<0:
                #如果为右重则先将右重的右子节点左旋，再将node右旋
                self.singleLeftRotate(node.leftchild)
                self.singleRightRotate(node)
            else:
                # 只需要右旋
                self.singleRightRotate(node)
    
    def singleLeftRotate(self,oldRoot):
        """右重左旋，node右重，打断为左子节点"""
        newRoot = oldRoot.rightchild
        oldRoot.rightchild = newRoot.leftchild
        #判断newRoot左子节点是否存在，若存在添加parent关系
        if newRoot.hasLeftChild():
            newRoot.leftchild.parent = oldRoot
        
        #改变newRoot的parent关系
        newRoot.parent = oldRoot.parent
        if oldRoot.isRoot():
            self.root = newRoot
        else:
            if oldRoot.isLeftChild:
                oldRoot.parent.leftchild = newRoot
            else:
                oldRoot.parent.rightchild = newRoot
        
        newRoot.leftchild = oldRoot
        oldRoot.parent = newRoot
        
        #调节平衡因子
        oldRoot.balanceFactor = oldRoot.balanceFactor +1 - min(newRoot.balanceFactor,0)
        newRoot.balanceFactor = newRoot.balanceFactor +1 + max(oldRoot.balanceFactor,0)
        
    def singleRightRotate(self,oldRoot):
        """左重右旋：树左重，oldRoot右旋为newRoot的右子树的根"""
        newRoot = oldRoot.leftchild
        oldRoot.leftchild = newRoot.rightchild
        
        if newRoot.hasRightChild():
            newRoot.rightchild.parent = oldRoot
        
        newRoot.rightchild = oldRoot
        
        #改变oldRoot的父节点关系
        if oldRoot.isRoot():
            self.root = newRoot
        else:
            if oldRoot.isLeftChild():
                oldRoot.parent.leftchild = newRoot
            else:
                oldRoot.parent.rightchild = newRoot
            
        newRoot.parent = oldRoot.parent
        oldRoot.parent = newRoot
        
        #调节平衡因子
        oldRoot.balanceFactor = oldRoot.balanceFactor -1 - max(newRoot.balanceFactor,0)
        newRoot.balanceFactor = newRoot.balanceFactor +1 + max(oldRoot.balanceFactor,0)
    
