# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:44:55 2023

@author: jerem
"""

import numpy as np
import matplotlib as mtp
from collections import deque

g1_vertex_list = {
            'a': ['b','c'],
            'b': ['a','d'],
            'c': ['a','d','f'],
            'd': ['b','c','e','S'],
            'e': ['d','h','r','S'],
            'f': ['c','G','r'],
            'G': ['f'],
            'h': ['e','p','q'],
            'p': ['h','q','S'],
            'q': ['h','p'],
            'r': ['e','f'],
            'S': ['d','e','p'],
            }

g1_adjacency_matrix = [[0,1,1,0,0,0,0,0,0,0,0,0],
                       [1,0,0,1,0,0,0,0,0,0,0,0],
                       [1,0,0,1,0,1,0,0,0,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,1],
                       [0,0,0,1,0,0,0,1,0,0,1,1],
                       [0,0,1,0,0,0,1,0,0,0,1,0],
                       [0,0,0,0,0,1,0,0,0,0,0,0],
                       [0,0,0,0,1,0,0,0,1,1,0,0],
                       [0,0,0,0,0,0,0,1,0,1,0,1],
                       [0,0,0,0,0,0,0,1,1,0,0,0],
                       [0,0,0,0,1,1,0,0,0,0,0,0],
                       [0,0,0,1,1,0,0,0,1,0,0,0],
                       ]

g2_vertex_list = {
            'a': [],
            'b': ['a'],
            'c': ['a'],
            'd': ['b','c','e'],
            'e': ['h','r'],
            'f': ['c','G'],
            'G': [],
            'h': ['p','q'],
            'p': ['q'],
            'q': [],
            'r': ['f'],
            'S': ['d','e','p'],    
    }
g2_adjacency_matrix = [[0,0,0,0,0,0,0,0,0,0,0,0],
                       [1,0,0,0,0,0,0,0,0,0,0,0],
                       [1,0,0,0,0,0,0,0,0,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1,0,0,1,0],
                       [0,0,1,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,1,0,0,0,0,0,0],
                       [0,0,0,1,1,0,0,0,1,0,0,0],
                       ]


g3_vertex_list = {
    'a': {'b': 2,'c': 2},
    'b': {'a':2,'d':1},
    'c': {'a': 2,'d': 8,'f': 3},
    'd': {'b':1,'c':8,'e':2,'S':3},
    'e': {'d':2,'h':8,'r':2,'S':9},
    'f': {'c':3,'G':2,'r':2},
    'G': {'f':2},
    'h': {'e':8,'p':4,'q':4},
    'p': {'h':4,'q':15,'S':1},
    'q': {'h':4,'p':15},
    'r': {'e':2,'f':2},
    'S': {'d':3,'e':9,'p':1},
    }
g3_adjacency_matrix = [[0,2,2,0,0,0,0,0,0,0,0,0],
                       [2,0,0,1,0,0,0,0,0,0,0,0],
                       [2,0,0,8,0,3,0,0,0,0,0,0],
                       [0,1,8,0,2,0,0,0,0,0,0,3],
                       [0,0,0,2,0,0,0,8,0,0,2,9],
                       [0,0,3,0,0,0,2,0,0,0,2,0],
                       [0,0,0,0,0,2,0,0,0,0,0,0],
                       [0,0,0,0,8,0,0,0,4,4,0,0],
                       [0,0,0,0,0,0,0,4,0,15,0,1],
                       [0,0,0,0,0,0,0,4,15,0,0,0],
                       [0,0,0,0,2,2,0,0,0,0,0,0],
                       [0,0,0,3,9,0,0,0,1,0,0,0],
                       ]


g4_vertex_list = {
    'a': {},
    'b': {'a':2},
    'c': {'a': 2},
    'd': {'b':1,'c':8,'e':2},
    'e': {'h':8,'r':2},
    'f': {'c':3,'G':2},
    'G': {},
    'h': {'p':4,'q':4},
    'p': {'q':15},
    'q': {},
    'r': {'f':2},
    'S': {'d':3,'e':9,'p':1},
    }

g4_adjacency_matrix = [[0,0,0,0,0,0,0,0,0,0,0,0],
                       [2,0,0,0,0,0,0,0,0,0,0,0],
                       [2,0,0,0,0,0,0,0,0,0,0,0],
                       [0,1,8,0,2,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,8,0,0,2,0],
                       [0,0,3,0,0,0,2,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,4,4,0,0],
                       [0,0,0,0,0,0,0,0,0,15,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,2,0,0,0,0,0,0],
                       [0,0,0,3,9,0,0,0,1,0,0,0],
                       ]

maps = {0: 'a',1: 'b', 2: 'c', 3:'d',4:'e',5:'f',6:'G',7:'h',8:'p',9:'q',10:'r',11:'S'}
visited = set()
parentMap={'S': None}

def DFS_Recursion_list(visited, graph, node, target):
    print(node, end=",")
    visited.add(node)
    for neighbor in graph[node]:
        if(neighbor not in visited):
            if(neighbor == target):
                print(neighbor)
                curr = target
                parentMap[curr]=node
                print("Path Returned:",end=" ")
                printStack = []
                while(curr!=None):
                    printStack.append(curr)
                    curr = parentMap[curr]
                while(len(printStack)>1):
                    pathNode = printStack[-1]
                    printStack.pop()
                    print(pathNode, end="-")
                pathNode = printStack[-1]
                printStack.pop();
                print(pathNode)
                return
            else:
                parentMap[neighbor]=node
                DFS_Recursion_list(visited, graph, neighbor, target)
    
def DFS_Loop_list(visited,graph,node, target):
    #print("In loop DFS")
    stack = []
    parentMap = {'S': None}
    stack.append(node)
    #visited.add(node)
    while(len(stack)>0):
        #print("Stack is", end=" ")
        #for val in stack:
        #    print(val,end=" ")
        #print()
        childStack = []
        v = stack[-1]
        #visited.add(v)
        stack.pop()
        #print(v, end ="-")
        if(v not in visited):
            print(v, end=",")
            visited.add(v)
            for neighbor in graph[v]:                       #here it reaches goal before node C
            #print(" Neighbor is ", neighbor)
                if(neighbor not in visited):
                    if(neighbor == target):
                        print(neighbor)
                        parentMap[neighbor] = v
                        stack = []
                        printStack = []
                        curr = target
                        print("Path Returned: ",end="")
                        while (curr!=None):
                            printStack.append(curr)
                            curr = parentMap[curr]
                        while(len(printStack)>1):
                            pathNode = printStack[-1]
                            printStack.pop()
                            print(pathNode, end="-")
                        pathNode = printStack[-1]
                        printStack.pop();
                        print(pathNode)
                        return
                    else:
                        childStack.append(neighbor)
                    #visited.add(neighbor)
            while(len(childStack)>0):
              child = childStack.pop()
              parentMap[child] = v
              #print(parentMap)
              stack.append(child)

def DFS_Recursion_Matrix(visited,graph,node,target):
    print(maps[node],end=',')
    visited[node]=True
    for i in range(len(graph[node])):
        if(graph[node][i]==1 and (not visited[i])):
            if(graph[node][i]==1 and i==target):
                print(maps[i])
                curr = target
                #print(curr)
                parentMap[curr]=node
                #print(parentMap[curr])
                print("Path Returned", end=" ")
                printStack = []
                while(curr!=None):
                    printStack.append(curr)
                    curr = parentMap[curr]
                while(len(printStack)>1):
                    pathNode=printStack[-1]
                    printStack.pop()
                    print(maps[pathNode],end="-")
                pathNode = printStack[-1]
                printStack.pop()
                print(maps[pathNode])
                return
            else:    
                parentMap[i]=node
                DFS_Recursion_Matrix(visited, graph, i, target)
    
def BFS_Recursion():
    print("In recursion BFS")
    
def BFS_Loop():
    print("In loop BFS")
    
def UCS():
    print("In UCS")
    
print("Recursion on Vertex List")
print()
print("States Expanded: ",end="")
DFS_Recursion_list(visited, g1_vertex_list, 'S', "G")
print("------------------")
visited = set()
parentMap={'S': None}
print("Iterative on Vertext List")
print()
print("States Expanded: ",end="")
DFS_Loop_list(visited, g1_vertex_list, 'S', 'G')
print("------------------")

visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11: None}
print("States Expanded", end=": ")
DFS_Recursion_Matrix(visited, g1_adjacency_matrix, 11, 6)