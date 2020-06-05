# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:12:34 2020

@author: yyuan
"""

class Node():
    """Node"""
    def __init__(self, elem = -1, lc = None, rc = None):
        self.elem = elem
        self.lchild = lc
        self.rchild = rc

class Tree():
    """Tree"""
    def __init__(self, root = None):
        self.root = root
    
    def add(self,elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            
            while queue:
                cur_node = queue.pop(0)
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.rchild)
    
    def breadth_travel(self):
        """广度优先遍历"""
        queue = [self.root]
        if queue is None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end = ' ')
        
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)  
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    
    def preorder(self, root):
        """深度优先前序遍历"""
        if root is None:
            return
        print(root.elem, end = ' ')
        #遍历左节点
        self.preorder(root.lchild)
        #遍历右节点
        self.preorder(root.rchild)
        
    def inorder(self,node):
        """深度优先中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        
        print(node.elem,end = ' ')
        
        self.inorder(node.rchild)
        
    def postorder(self,node):
        if node is None:
            return
        
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end = ' ')

if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    """
                1
            2       3
          4   5   6   7
        8  9
    """
    tree.breadth_travel()
    print('')
    tree.preorder(tree.root)
    print('')
    tree.inorder(tree.root)
    print('')
    tree.postorder(tree.root)
    print('')
    
     




a = int(input())
a = list[a]
print(sum(a))       
