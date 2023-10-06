# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:09:56 2023

@author: jerem
"""

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = 0

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

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeId())
            printTree(tree.getRightChild())

def testTree():
    myTree = BinaryTree("l_0")
    myTree.insertLeft("l_10")
    myTree.insertRight("l_11")
    l10 = myTree.getLeftChild()
    l10.insertLeft("l_20")
    l10.insertRight("l_21")
    l11 = myTree.getRightChild()
    l11.insertLeft("l_22")
    l11.insertRight("l_23")

    printTree(myTree)

#testTree()