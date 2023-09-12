# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:44:55 2023

@author: jerem
"""

from collections import deque
import heapq

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


def DFS_Recursion_list(visited, graph, node, target):
    print(node, end=",")                            
    visited.add(node)                                                   #marking current node as visited
    for neighbor in graph[node]:                                        #cycle through neighbors of current node
        if(neighbor not in visited):    
            if(neighbor == target):                                     #if the neighbor is the target, then print the neighbor to complete States Expanded
                print(neighbor)                             
                curr = target
                parentMap[curr]=node
                print("Path Returned:",end=" ")
                printStack = []
                while(curr!=None):                                      #add parents from target to start node to printStack
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
                parentMap[neighbor]=node                                #add current node to neighbor's parentMap
                DFS_Recursion_list(visited, graph, neighbor, target)    #recursively call DFS on neighbor nodes
  
def DFS_Loop_list(visited,graph,node, target):
    stack = []                                              
    parentMap = {'S': None}
    stack.append(node)                                      #add starting node to stack
    while(len(stack)>0):
        childStack = []
        v = stack[-1]
        stack.pop()
        if(v not in visited):
            print(v, end=",")
            visited.add(v)                                  #mark LIFO node as visited
            for neighbor in graph[v]:                      
                if(neighbor not in visited):
                    if(neighbor == target):                 #if node is the target, then print to finish States Expanded
                        print(neighbor)
                        parentMap[neighbor] = v
                        stack = []
                        printStack = []
                        curr = target
                        print("Path Returned: ",end="")
                        while (curr!=None):                 #add parents from target node all the way to starting node to printStack
                            printStack.append(curr)
                            curr = parentMap[curr]
                        while(len(printStack)>1):
                            pathNode = printStack[-1]
                            printStack.pop()
                            print(pathNode, end="-")
                        pathNode = printStack[-1]
                        printStack.pop();
                        print(pathNode)                     #print path
                        return
                    else:
                        childStack.append(neighbor)         #if neighbor is not target, add it to child stack
            while(len(childStack)>0):                   
              child = childStack.pop()                      #move neighbors from child stack to main stack to maintain ordering
              parentMap[child] = v
              stack.append(child)

def DFS_Recursion_Matrix(visited,graph,node,target):
    print(maps[node],end=',')
    visited[node]=True
    for i in range(len(graph[node])):                               #instead of looping through list of neighbors, loop through all indices in adjacency matrix
        if(graph[node][i]==1 and (not visited[i])):
            if(graph[node][i]==1 and i==target):                    #if index is the target index, then print the node at the index and print the path to the target
                print(maps[i])
                curr = target
                parentMap[curr]=node
                print("Path Returned", end=": ")
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
                parentMap[i]=node                                   #add current node index to neighbors parentMap
                DFS_Recursion_Matrix(visited, graph, i, target)     #recursively call DFS on neighbors
    
def DFS_Loop_Matrix(visited, graph, node, target):
    stack=[]
    parentMap = {11: None}
    stack.append(node)                                      #add starting node to stack
    childStack=[]
    while(len(stack)>0):
        v = stack[-1]
        stack.pop()
        if(visited[v]==False):                                  
            print(maps[v], end=",")
            visited[v]=True                                 #mark node popped out of stack as visited
            for i in range(len(graph[v])):
                if(graph[v][i]==1 and (not visited[i])):    #if index in adjacency row of node is 1 and that index hasn't been visited
                    if(graph[v][i]==1 and i==target):       #if index is target, then print that index node to finish States Expanded, and the path to the target from Start
                        print(maps[i])
                        curr=i
                        parentMap[curr]=v
                        stack=[]
                        print("Path Returned", end=": ")
                        printStack=[]
                        while(curr!=None):
                            printStack.append(curr)
                            curr=parentMap[curr]
                        while(len(printStack)>1):
                            pathNode = printStack[-1]
                            printStack.pop()
                            print(maps[pathNode],end="-")
                        pathNode=printStack[-1]
                        printStack.pop()
                        print(maps[pathNode])
                        return;
                    else:
                        childStack.append(i)                #if index is not target, add index to child Stack
                        parentMap[i]=v
            while(len(childStack)>0):
                child = childStack[-1]
                childStack.pop()
                parentMap[child]=v
                stack.append(child)                         #add child from childstack to main stack to maintain ordering
    
def BFS_Recursion_List(visited, graph, target, queue):
    node = queue[0]                                             
    if(node not in visited):                                            
        print(node,end=",")
        queue.popleft()                                         
        visited.add(node)                               #if node at start of queue is not visited, then mark as visited
        for neighbor in graph[node]:
            if(neighbor not in visited):
                if(neighbor==target):                   #if neighbor is target, then print neighbor to finish States Expanded
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
                    print(pathNode)                     #print path from Start to target node
                    return
                else:
                    if(neighbor not in parentMap):
                        parentMap[neighbor]=node        #add curr node to neighbors parent map only if there isnt a shorter path to the neighbor already in parentMap
                    queue.append(neighbor)
        BFS_Recursion_List(visited, graph, target, queue)   #recursively call BFS 
    else:
        queue.popleft()                                 #remove node from queue if visited
        BFS_Recursion_List(visited,graph,target,queue)  #recursively call BFS
    
def BFS_Loop_List(visited, graph, target, queue):
    while(len(queue)>0):                                        #while bfs queue isn't empty keep running
        node = queue[0]
        queue.popleft()
        if(node not in visited):
            print(node,end=",")
            visited.add(node)
            for neighbor in graph[node]:                        #loop through neighbors in vertex list
                if(neighbor not in visited):
                    if(neighbor==target):                       #if neighbor is the target, print to finish States Expanded
                        print(neighbor)
                        parentMap[neighbor] = node
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
                        print(pathNode)                         #print path from Start to Target
                        return
                    else:
                        if(neighbor not in parentMap):
                            parentMap[neighbor]=node           #only add nodeto neighbor parent map if there isn't a shorter path to the neighbor
                        queue.append(neighbor)                 #add neighbor to queue
            
def BFS_Recursion_Matrix(visited, graph, target, queue):
    node = queue[0]
    queue.popleft()
    if(node==target):
        print(maps[node])
        print("Path Returned: ",maps[node])                 #if start node is target, then print node as path
        return
    if(not visited[node]):
        print(maps[node], end=",")
        visited[node]=True
        for i in range(len(graph[node])):                   #loop through indices in graph[node]
            if(graph[node][i]==1 and (not visited[i])):
                if(i==target):                              #if index i points to target, print target to finish States Expanded
                    print(maps[i])
                    curr = target
                    parentMap[curr]=node
                    print("Path Returned", end=": ")
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
                    print(maps[pathNode])                   #print path from Start to Target
                    return
                else:
                    if( i not in parentMap):                #only add node as neighbor's parent if there isn't a shorter path to the neighbor
                        parentMap[i]=node
                    queue.append(i)                         #add neighbor index to queue
    BFS_Recursion_Matrix(visited,graph,target,queue)        #recursively call BFS with updated queue
        
def BFS_Loop_Matrix(visited, graph, target, queue):
    while(len(queue)>0):                                        #loop till queue is empty
        node = queue[0]
        queue.popleft()
        if(not visited[node]):
            print(maps[node],end=",")
            visited[node]=True
            for i in range(len(graph[node])):                   #loop through indices of graph[node] row in adjacency matrix
                if(graph[node][i]==1 and (not visited[i])):     
                    if(i==target):                              #if index is target index, then print node at index to finish States Expanded
                        print(maps[i])
                        curr = target
                        parentMap[curr]=node
                        print("Path Returned", end=": ")
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
                        print(maps[pathNode])                   #print path from Start node to Target node
                        return
                    else:
                        if(i not in parentMap):                 #only add node index as neighbor index parent if there isn't a shorter path
                            parentMap[i]=node
                        queue.append(i)                         #add neighbor index to queue
    
def UCS_list(graph, start, target):
    visited = set()
    q = []
    heapq.heappush(q,(0,start,[start]))                     #create heap with tuple of (Priority, node, and array of path to node)
    while(len(q)>0):
        prio,curr, path= heapq.heappop(q)                   #get highest prio (lowest priority number) tuple
        if(curr not in visited):
            visited.add(curr)                               #if current node isn't visited, then add to visited
            if(curr == target):
                print(curr)                                 #if current node is target, then print node to finish States Expanded
                print("Path Returned: ", end="")
                for i in range(len(path)-1):
                    print(path[i],end="-")
                print(path[len(path)-1])                    #print path to target node
                q = []                                      #empty queue
            else:
                print(curr, end=",")
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        heapq.heappush(q,(prio+graph[curr][neighbor],neighbor, path+[neighbor]))        #push neighbor to heap with curr prio + neighbor edge weight as new prio
        
            
def UCS_matrix(graph, start, target):
    visited = [False]*len(graph[0])
    q = []
    heapq.heappush(q,(0,start,[maps[start]]))                                           #create heap with tuple (priority, node, path to node)
    while(len(q)>0):
        prio,curr,path = heapq.heappop(q)                                               #get highest prio tuple (lowest priority number)
        if(visited[curr]==False):
            visited[curr]=True
            if(curr==target):
                print(maps[curr])                                                       #if node is target, print to finish States Expanded
                print("Path Returned: ", end="")
                for i in range(len(path)-1):
                    print(path[i],end="-")
                print(path[len(path)-1])                                                #print path to target
                q = []  
            else:
                print(maps[curr],end=",")
                for i in range(len(graph[curr])):
                    if graph[curr][i]>0 and visited[i]==False:
                        heapq.heappush(q,(prio+graph[curr][i], i, path+[maps[i]]))      #push tuple to heap with current prio + matrix cell value as new priority


#DFS Recursion on G1 Vertex List
visited = set()
parentMap={'S': None}
print()
print("DFS Recursion on G1 Vertex List")
print("States Expanded: ",end="")
DFS_Recursion_list(visited, g1_vertex_list, 'S', "G")
print()
print("-------------------------------------------")

#DFS Loop on G1 Vertex List
visited = set()
parentMap={'S': None}
print("DFS Loop on G1 Vertex List")
print("States Expanded: ",end="")
DFS_Loop_list(visited, g1_vertex_list, 'S', 'G')
print("-------------------------------------------")

#BFS Recursion on G1 Vertex List
queue = deque()
queue.append('S')
visited = set()
parentMap = {'S':None}
print("BFS Recursion on G1 Vertex List")
print("States Expanded", end=": ")
BFS_Recursion_List(visited, g1_vertex_list, 'G', queue)
print()
print("-------------------------------------------")

#BFS Loop on G1 Vertex List
queue = deque()
queue.append('S')
visited = set()
parentMap = {'S':None}
print("BFS Loop on G1 Vertex List")
print("States Expanded", end=": ")
BFS_Loop_List(visited, g1_vertex_list, 'G', queue)
print()
print("-------------------------------------------")
print("-------------------------------------------")

#DFS Recursion on G1 Adjacency Matrix
visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11: None}
print("DFS Recursion on G1 adjacency matrix")
print("States Expanded", end=": ")
DFS_Recursion_Matrix(visited, g1_adjacency_matrix, 11, 6)
print()
print("-------------------------------------------")

#DFS Loop on G1 Adjacency Matrix
visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11:None}
print("DFS Loop on G1 adjacency matrix")
print("States Expanded",end=": ")
DFS_Loop_Matrix(visited, g1_adjacency_matrix, 11, 6)
print()
print("-------------------------------------------")

#BFS Recursion on G1 Adjacency Matrix
queue = deque()
queue.append(11)
visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11: None}
print("BFS Recursion on G1 adjacency matrix")
print("States Expanded", end=": ")
BFS_Recursion_Matrix(visited, g1_adjacency_matrix, 6, queue)
print()
print("-------------------------------------------")

#BFS Loop on G1 Adjacency Matrix
queue = deque()
queue.append(11)
visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11:None}
print("BFS Loop on G1 adjacency matrix")
print("States Expanded",end=": ")
BFS_Loop_Matrix(visited, g1_adjacency_matrix, 6, queue)
print()
print("-------------------------------------------")

print("-------------------------------------------")
print("-------------------------------------------")

#DFS Recursion on G2 Vertex List
visited = set()
parentMap={'S': None}
print()
print("DFS Recursion on G2 Vertex List")
print("States Expanded: ",end="")
DFS_Recursion_list(visited, g2_vertex_list, 'S', "G")
print()
print("-------------------------------------------")

#DFS Loop on G2 Vertex List
visited = set()
parentMap={'S': None}
print("DFS Loop on G2 Vertex List")
print("States Expanded: ",end="")
DFS_Loop_list(visited, g2_vertex_list, 'S', 'G')
print("-------------------------------------------")

#BFS Recursion on G2 Vertex List
queue = deque()
queue.append('S')
visited = set()
parentMap = {'S':None}
print()
print("BFS Recursion on G2 Vertex List")
print("States Expanded: ",end="")
BFS_Recursion_List(visited, g2_vertex_list, "G", queue)
print()
print("-------------------------------------------")

#BFS Loop on G2 Vertex List
queue = deque()
queue.append('S')
visited = set()
parentMap = {'S':None}
print("BFS Loop on G2 Vertex List")
print("States Expanded: ",end="")
BFS_Loop_List(visited, g2_vertex_list, 'G', queue)
print("-------------------------------------------")
print("-------------------------------------------")

#DFS Recursion on G2 Adjacency Matrix
visited = [False]*len(g2_adjacency_matrix[0])
parentMap={11: None}
print("DFS Recursion on G2 adjacency matrix")
print("States Expanded", end=": ")
DFS_Recursion_Matrix(visited, g2_adjacency_matrix, 11, 6)
print()
print("-------------------------------------------")

#DFS Loop on G2 Adjacency Matrix
visited = [False]*len(g2_adjacency_matrix[0])
parentMap={11:None}
print("DFS Loop on G2 adjacency matrix")
print("States Expanded",end=": ")
DFS_Loop_Matrix(visited, g2_adjacency_matrix, 11, 6)
print()
print("-------------------------------------------")

#BFS Recursion on G2 Adjacency Matrix
queue = deque()
queue.append(11)
visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11:None}
print()
print("BFS Recursion on G2 adjacency matrix")
print("States Expanded: ",end="")
BFS_Recursion_Matrix(visited, g2_adjacency_matrix, 6, queue)
print()
print("-------------------------------------------")

#BFS Loop on G2 Adjacency Matrix
queue = deque()
queue.append(11)
visited = [False]*len(g1_adjacency_matrix[0])
parentMap={11:None}
print("BFS Loop on G2 adjacency matrix")
print("States Expanded: ",end="")
BFS_Loop_Matrix(visited, g2_adjacency_matrix, 6, queue)
print("-------------------------------------------")

print("-------------------------------------------")
print("-------------------------------------------")

#UCS On G3 Vertex List
print("UCS on G3 Vertex List")
print("States expanded: ", end="")
UCS_list(g3_vertex_list, "S", 'G')
print()
print("-------------------------------------------")

#UCS On G3 Adjacency Matrix
print("UCS on G3 Adjacency Matrix")
print("States expanded: ", end="")
UCS_matrix(g3_adjacency_matrix, 11, 6)
print()
print("-------------------------------------------")
print("-------------------------------------------")

#UCS on G4 Vertex List
print("UCS on G4 Vertex List")
print("States expanded: ", end="")
UCS_list(g4_vertex_list, "S", 'G')
print()
print("-------------------------------------------")

#UCS On G4 Adjacency Matrix
print("UCS on G4 Adjacency Matrix")
print("States expanded: ", end="")
UCS_matrix(g4_adjacency_matrix, 11, 6)
print()
print("-------------------------------------------")
print("-------------------------------------------")

#Bugs and questions
#DFS Recrusion keeps searching through nodes after path is returned
#UCS on G4 Vertex list does not search state c, but adjacency matrix does