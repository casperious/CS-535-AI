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


def value(node,state):
    if(node.getLeftChild()==None and node.getRightChild()==None):
        return node.getNodeValue()
    elif(state=="Min"):                                                         #if curr state is Min, then next states are max
        node.setNodeValue(float('inf'))
        leftVal,leftNode, leftPath = max_value(node.getLeftChild(),[])
        rightVal,rightNode, rightPath = max_value(node.getRightChild(),[])
        minVal= min(node.getNodeValue(),leftVal,rightVal)
    elif(state=="Max"):
        node.setNodeValue(float("-inf"))
        leftVal,leftNode, leftPath = min_value(node.getLeftChild(),[])
        rightVal,rightNode, rightPath = min_value(node.getRightChild(),[])
        retPath = []
        maxVal = max(node.getNodeValue(),leftVal,rightVal)
        if(leftVal>rightVal):
            retPath = leftPath
            retNode = leftNode
        else:
            retPath = rightPath
            retNode = rightNode
    retPath.append(node.getNodeId())
    print(retPath)
    return retNode
        
def min_value(node,path):
    if(node==None):
        return float('-inf')
    if(node.getLeftChild()==None and node.getRightChild()==None):
         retPath = [node.getNodeId()]
         path.append(node.getNodeId())
         return node.getNodeValue(),node, retPath
    node.setNodeValue(float("inf"))
    leftVal,leftNode, leftPath = max_value(node.getLeftChild(),path)
    rightVal,rightNode, rightPath = max_value(node.getRightChild(),path)
    val = min(node.getNodeValue(),leftVal,rightVal)
    retPath = []
    retNode = 0
    if(val==node.getNodeValue()):
        print("Not adding to path")
    elif(leftVal<rightVal):
        retPath = leftPath
        retNode = leftNode
    else:
        retPath = rightPath
        retNode = rightNode
    node.setNodeValue = val
    retPath.append(node.getNodeId())
    return val,retNode,retPath
    
def max_value(node,path):
    if(node==None):
        return float("inf")
    if(node.getLeftChild()==None and node.getRightChild()==None):
        retPath = [node.getNodeId()]
        path.append(node.getNodeId())
        return node.getNodeValue(),node, retPath
    node.setNodeValue(float("-inf"))
    leftVal,leftNode, leftPath = min_value(node.getLeftChild(),path)
    rightVal,rightNode, rightPath = min_value(node.getRightChild(),path)
    val =  max(node.getNodeValue(),leftVal,rightVal)
    retPath = []
    retNode = 0
    if(val==node.getNodeValue()):
        print("Not adding to path")
    elif(leftVal>rightVal):
        retPath = leftPath
        retNode = leftNode
    else:
        retPath = rightPath
        retNode = rightNode
    node.setNodeValue = val
    retPath.append(node.getNodeId())
    return val,retNode,retPath


def ab_pruning(node,depth,state,alpha,beta):
    if(node.getLeftChild()==None and node.getRightChild()==None):               #leaf node, return value of node
        return node.getNodeValue(),node.getNodeId()
    if(state == "Max"):
        bestVal = float("-inf")
        for i in range (0,2):
            if(i%2==0):                                                             #left child
                val,leaf = ab_pruning(node.getLeftChild(), depth+1, "Min", alpha, beta)
            else:                                                                   #right child
                val,leaf = ab_pruning(node.getRightChild(), depth+1, "Min", alpha, beta)
            if(val>bestVal):
                retNode = leaf
            bestVal = max(val,bestVal)
            alpha = max(alpha,bestVal)                                              #update alpha
            if(beta<=alpha):                                                        #if 
                break
        return bestVal,retNode
    else:
        bestVal = float("inf")
        for i in range(0,2):
            if(i%2==0):
                val,leaf = ab_pruning(node.getLeftChild(), depth+1, "Max", alpha, beta)
            else:
                val,leaf = ab_pruning(node.getRightChild(), depth+1, "Max", alpha, beta)
            if(val<bestVal):
                retNode = leaf
            bestVal = min(bestVal,val)
            beta = min(bestVal,beta)
            if(beta<=alpha):
                break
        return bestVal,retNode
    

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

print("Minimax Q3.1")

print("Output Path:- ")
output = value(tree,"Max")
print("Output:- ")
print(output.getNodeValue())


print("-------------------------------------------------------------------------")

print()

print("Alpha Beta Pruning Q3.3")
bestVal,retNode = ab_pruning(tree, 0, "Max", float("-inf"), float("inf"))
print(bestVal)