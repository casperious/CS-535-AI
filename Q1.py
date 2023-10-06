# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:27:54 2023

@author: jerem
"""

from collections import deque
import heapq

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

def h(node):
    match node:
        case "a":
            return 5    
        case "b":
            return 7
        case "c":
            return 4
        case "d":
            return 7
        case "e":
            return 5
        case "f":
            return 2
        case "G":
            return 0
        case "h":
            return 11
        case "p":
            return 14
        case "q":
            return 12
        case "r":
            return 3
        case "S":
            return 10
        

ended = False
finalPath=[]

def Greedy(start,target,graph):
    visited = set()
    cost = 0
    q = []
    heapq.heappush(q,(10,start,[start]))                     #create heap with tuple of (Priority, node, and array of path to node)
    while(len(q)>0):
        prio,curr, path= heapq.heappop(q)                   #get highest prio (lowest priority number) tuple
        cost+=prio
        if(curr not in visited):
            visited.add(curr)
            if(curr == target):
                print(curr,end=",")                         #if current node is target, then print node to finish States Expanded
                global finalPath
                finalPath= path                             #set final path to shortest path to goal
                print()
                print("Path Returned: ", end="")
                for i in range(len(finalPath)-1):           #print final path
                    print(finalPath[i],end="-")
                print(finalPath[len(finalPath)-1])          #print path to target node
                print("cost is ",cost)
                return
            else:
                print(curr, end=",")
                for neighbor in graph[curr]:                #loop through neighbors in vertex list
                    if neighbor not in visited:
                        heapq.heappush(q,(h(neighbor),neighbor, path+[neighbor]))        #push neighbor to heap with h(neighbor) as new prio
            
    
    
def A_Star(start, target, graph):
    visited = set()
    cost = 0
    q = []
    heapq.heappush(q,(10,start,[start]))                     #create heap with tuple of (Priority, node, and array of path to node)
    while(len(q)>0):
        prio,curr, path= heapq.heappop(q)                   #get highest prio (lowest priority number) tuple
        cost+=prio
        if(curr not in visited):
            visited.add(curr)
            if(curr == target):
                print(curr,end=",")                         #if current node is target, then print node to finish States Expanded
                global finalPath
                finalPath= path                             #set final path to shortest path to goal
                print()
                print("Path Returned: ", end="")
                for i in range(len(finalPath)-1):           #print final path
                    print(finalPath[i],end="-")
                print(finalPath[len(finalPath)-1])          #print path to target node
                print("cost is ",cost)
                return
            else:
                print(curr, end=",")
                for neighbor in graph[curr]:                #loop through neighbors in vertex list
                    if neighbor not in visited:
                        heapq.heappush(q,(h(neighbor) + graph[curr][neighbor],neighbor, path+[neighbor]))        #push neighbor to heap with h(neighbor)+dist to neighbor as new prio
            

finalPath=[]
print("Greedy on G3 Vertex List")
print("States expanded: ", end="")
Greedy("S", 'G',g3_vertex_list)
print()
print("-------------------------------------------")

finalPath=[]
print("A* on G3 Vertex List")
print("States expanded: ", end="")
A_Star("S", 'G',g3_vertex_list)
print()
print("-------------------------------------------")

