# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:09:56 2023

@author: jerem
"""

class BinaryTree():

    def __init__(self,rootid,value):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = value

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.value = value
    def getNodeValue(self):
        return self.value
    def getNodeId(self):
        return self.rootid

    def insertRight(self,newNode,value):
        if self.right == None:
            self.right = BinaryTree(newNode,value)
        else:
            tree = BinaryTree(newNode,value)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode,value):
        if self.left == None:
            self.left = BinaryTree(newNode,value)
        else:
            tree = BinaryTree(newNode,value)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())

def testTree():
    myTree = BinaryTree("l_0",0)
    myTree.insertLeft("l_10",1)
    myTree.insertRight("l_11",2)
    l10 = myTree.getLeftChild()
    l10.insertLeft("l_20",3)
    l10.insertRight("l_21",4)
    l11 = myTree.getRightChild()
    l11.insertLeft("l_22",5)
    l11.insertRight("l_23",6)

    printTree(myTree)

#testTree()

def value(node,state):
    if(node.getLeftChild()==None and node.getRightChild()==None):
        return node.getNodeValue()
    elif(state=="Min"):                                                         #if curr state is Min, then next states are max
        node.setNodeValue(float('inf'))
        return min(node.getNodeValue(),max_value(node.getLeftChild()),max_value(node.getRightChild()))
    elif(state=="Max"):
        node.setNodeValue(float("-inf"))
        return max(node.getNodeValue(),min_value(node.getLeftChild()),min_value(node.getRightChild()))
        
def min_value(node):
    if(node==None):
        return float('-inf')
    #node.value = float("inf") 
    if(node.getLeftChild()==None and node.getRightChild()==None):
         print("min val for ",node.getNodeId()," is ", node.getNodeValue())
         return node.getNodeValue()
    node.setNodeValue(float("inf"))
    val = min(node.getNodeValue(),max_value(node.getLeftChild()),max_value(node.getRightChild()))
    print("min val for ",node.getNodeId()," is ", val)
    node.setNodeValue = val
    return val
    
def max_value(node):
    if(node==None):
        return float("inf")
    #node.value = float("-inf")
    if(node.getLeftChild()==None and node.getRightChild()==None):
        print("max val for ",node.getNodeId()," is ", node.getNodeValue())
        return node.getNodeValue()
    node.setNodeValue(float("-inf"))
    val =  max(node.getNodeValue(),min_value(node.getLeftChild()),min_value(node.getRightChild()))
    print("max val for ",node.getNodeId()," is ", val)
    node.setNodeValue(val)
    return val

'''def alpha_beta_pruning(node,state):
    if(node.getLeftChild()==None and node.getRightChild()==None):
        return node.getNodeValue()
    elif(state=="Min"):                                                         #if curr state is Min, then next states are max
        node.setNodeValue(float('inf'))
        return min(node.getNodeValue(),max_value_ab(node.getLeftChild()),max_value_ab(node.getRightChild()))
    elif(state=="Max"):
        node.setNodeValue=float("-inf")
        return max(node.getNodeValue(),min_value_ab(node.getLeftChild()),min_value_ab(node.getRightChild()))
    
def min_value_ab(node,alpha,beta):
    print("ab min")
    if(node==None):
        return float('-inf')
    #node.value = float("inf") 
    if(node.getLeftChild()==None and node.getRightChild()==None):
         print("min val for ",node.getNodeId()," is ", node.getNodeValue())
         return node.getNodeValue()
    node.setNodeValue(float("inf"))
    val = min(node.getNodeValue(),max_value_ab(node.getLeftChild(),alpha,beta),max_value_ab(node.getRightChild(),alpha,beta))
    print("min val for ",node.getNodeId()," is ", val)
    if(val<=alpha):
        node.setNodeValue = val
    beta = min(beta,val)
    return val

def max_value_ab(node,alpha,beta):
    print("max ab")
    if(node==None):
        return float("inf")
    #node.value = float("-inf")
    if(node.getLeftChild()==None and node.getRightChild()==None):
        print("max val for ",node.getNodeId()," is ", node.getNodeValue())
        return node.getNodeValue()
    node.setNodeValue(float("-inf"))
    val =  max(node.getNodeValue(),min_value_ab(node.getLeftChild(),alpha,beta),min_value_ab(node.getRightChild(),alpha,beta))
    print("max val for ",node.getNodeId()," is ", val)
    if(val>=beta):
        node.setNodeValue(val)
    alpha = max(alpha,val)
    return val
'''

def ab_pruning(node,depth,state,alpha,beta):
    if(node.getLeftChild()==None and node.getRightChild()==None):               #leaf node, return value of node
        return node.getNodeValue()
    if(state == "Max"):
        bestVal = float("-inf")
        for i in range (0,2):
            if(i%2==0):                                                             #left child
                val = ab_pruning(node.getLeftChild(), depth+1, "Min", alpha, beta)
            else:                                                                   #right child
                val = ab_pruning(node.getRightChild(), depth+1, "Min", alpha, beta)
            bestVal = max(val,bestVal)
            alpha = max(alpha,bestVal)                                              #update alpha
            if(beta<=alpha):
                break
        return bestVal
    else:
        bestVal = float("inf")
        for i in range(0,2):
            if(i%2==0):
                val = ab_pruning(node.getLeftChild(), depth+1, "Max", alpha, beta)
            else:
                val = ab_pruning(node.getRightChild(), depth+1, "Max", alpha, beta)
            bestVal = min(bestVal,val)
            beta = min(bestVal,beta)
            if(beta<=alpha):
                break
        return bestVal
    

tree = BinaryTree("Root",0)
tree.insertLeft("H_1_L",0)
tree.insertRight("H_1_R",0)

l1 = tree.getLeftChild()
r1 = tree.getRightChild()

l1.insertLeft("H_2_L_L",0)
l1.insertRight("H_2_L_R",0)
r1.insertLeft("H_2_R_L",0)
r1.insertRight("H_2_R_R",0)

l2l = l1.getLeftChild()
l2r = l1.getRightChild()
r2l = r1.getLeftChild()
r2r = r1.getRightChild()

l2l.insertLeft("H_3_L_L_L",0)
l2l.insertRight("H_3_L_L_R",0)
l2r.insertLeft("H_3_L_R_L",0)
l2r.insertRight("H_3_L_R_R",0)
r2l.insertLeft("H_3_R_L_L", 0)
r2l.insertRight("H_3_R_L_R",0)
r2r.insertLeft("H_3_R_R_L",0)
r2r.insertRight("H_3_R_R_R",0)

HLLL = l2l.getLeftChild()
HLLR = l2l.getRightChild()
HLRL = l2r.getLeftChild()
HLRR = l2r.getRightChild()
HRLL = r2l.getLeftChild()
HRLR = r2l.getRightChild()
HRRL = r2r.getLeftChild()
HRRR = r2r.getRightChild()

HLLL.insertLeft("Leaf_1",3)
HLLL.insertRight("Leaf_2",10)
HLLR.insertLeft("Leaf_3",2)
HLLR.insertRight("Leaf_4",9)
HLRL.insertLeft("Leaf_5",10)
HLRL.insertRight("Leaf_6",7)
HLRR.insertLeft("Leaf_7",5)
HLRR.insertRight("Leaf_8",9)
HRLL.insertLeft("Leaf_9",2)
HRLL.insertRight("Leaf_10",5)
HRLR.insertLeft("Leaf_11",6)
HRLR.insertRight("Leaf_12",4)
HRRL.insertLeft("Leaf_13",2)
HRRL.insertRight("Leaf_14",7)
HRRR.insertLeft("Leaf_15",9)
HRRR.insertRight("Leaf_16",1)

#printTree(tree)

output = value(tree,"Max")
print(output)

abPruning = ab_pruning(tree, 0, "Max", float("-inf"), float("inf"))
print(abPruning)