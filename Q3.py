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

'''

value(node,state): This function takes in the root node, and the state to start at (Min or Max)
Calls min_value on children if starting state is max, set root node value to min of children and itself
Calls max_value on children if starting state is min, set root node value to max of children and itself

'''

def value(node,state):
    if(node.getLeftChild()==None and node.getRightChild()==None):
        return node.getNodeValue()
    elif(state=="Min"):                                                         #if curr state is Min, then next states are max
        node.setNodeValue(float('inf'))
        leftVal,leftNode, leftPath = max_value(node.getLeftChild(),[])          #start recursive call of minimax on left node
        rightVal,rightNode, rightPath = max_value(node.getRightChild(),[])      #start recursive call of minimax on right node
        minVal= min(node.getNodeValue(),leftVal,rightVal) 
        node.setNodeValue(minVal)                                               #set root value
        if(leftVal<rightVal):                                                   #compare both values, choose the path and node of the lower
            retPath = leftPath
            retNode = leftNode
        else:
            retPath = rightPath
            retNode = rightNode
    elif(state=="Max"):
        node.setNodeValue(float("-inf"))
        leftVal,leftNode, leftPath = min_value(node.getLeftChild(),[])          #start recursive call of minimax on left node
        rightVal,rightNode, rightPath = min_value(node.getRightChild(),[])      #start recursive call of minimax on right node
        retPath = []
        maxVal = max(node.getNodeValue(),leftVal,rightVal)
        node.setNodeValue(maxVal)                                               #set root value
        if(leftVal>rightVal):                                                   #compare both values, choose the path and node of the higher
            retPath = leftPath
            retNode = leftNode
        else:
            retPath = rightPath
            retNode = rightNode
    retPath.append(node.getNodeId())
    print(retPath)                                                              #print path to terminal leaf node
    return retNode
        
'''

min_value gets the minimum of its childrens values. If the node passed in is a leaf, then it starts the return path from the leaf, and returns 
the value, the node object, and the retPath

'''

def min_value(node,path):
    if(node==None):
        return float('-inf')
    if(node.getLeftChild()==None and node.getRightChild()==None):                   #Leaf node
         retPath = [node.getNodeId()]                                               #Create path array starting at leaf
         path.append(node.getNodeId())
         return node.getNodeValue(),node, retPath
    node.setNodeValue(float("inf"))                                                 #Subtree node. Set value to +infinity
    leftVal,leftNode, leftPath = max_value(node.getLeftChild(),path)                #call max_value on left child
    rightVal,rightNode, rightPath = max_value(node.getRightChild(),path)            #call max_value on right child
    val = min(node.getNodeValue(),leftVal,rightVal)                                 #get min of +inf, left and right child
    retPath = []
    retNode = 0
    if(val==node.getNodeValue()):
        print("Not adding to path")
    elif(leftVal<rightVal):                                                         #compare left and right values, and choose the lower value path and node to return
        retPath = leftPath
        retNode = leftNode
    else:
        retPath = rightPath
        retNode = rightNode
    node.setNodeValue = val
    retPath.append(node.getNodeId())                                                #add this node to the path and return
    return val,retNode,retPath
           
'''

max_value gets the maximum of its childrens values. If the node passed in is a leaf, then it starts the return path from the leaf, and returns 
the value, the node object, and the retPath

'''
 
def max_value(node,path):
    if(node==None):
        return float("inf")
    if(node.getLeftChild()==None and node.getRightChild()==None):                   #Leaf node
        retPath = [node.getNodeId()]                                                #create path array starting at leaf
        path.append(node.getNodeId())
        return node.getNodeValue(),node, retPath
    node.setNodeValue(float("-inf"))                                                #subtree node. set value to -infinity
    leftVal,leftNode, leftPath = min_value(node.getLeftChild(),path)                #call min_value on left child
    rightVal,rightNode, rightPath = min_value(node.getRightChild(),path)            #call min_value on right child
    val =  max(node.getNodeValue(),leftVal,rightVal)                                #get max of -inf, left and right child
    retPath = []
    retNode = 0
    if(val==node.getNodeValue()):
        print("Not adding to path")
    elif(leftVal>rightVal):                                                         #compare left and right values, and choose the higher value path and node to return
        retPath = leftPath
        retNode = leftNode
    else:
        retPath = rightPath
        retNode = rightNode
    node.setNodeValue = val
    retPath.append(node.getNodeId())                                                #add this node to the path and return
    return val,retNode,retPath

'''

ab_pruning performs alpha beta pruning on given binary tree.
Accepts the node, its depth, the state "Min" or "Max", the alpha and beta values

'''

def ab_pruning(node,depth,state,alpha,beta):
    if(node.getLeftChild()==None and node.getRightChild()==None):                       #leaf node
        return node.getNodeValue(),node.getNodeId()                                     #Return leaf value and name                
    if(state == "Max"):                                                                 #Max node                
        bestVal = float("-inf")                                                         #set initial value to -infinity        
        for i in range (0,2):                                                           #loop through children                
            if(i%2==0):                                                                 #left child first
                val,leaf = ab_pruning(node.getLeftChild(), depth+1, "Min", alpha, beta)
            else:                                                                       #right child second
                val,leaf = ab_pruning(node.getRightChild(), depth+1, "Min", alpha, beta)
            if(val>bestVal):                                                            #if value of child is greater than current bestVal
                retNode = leaf                                                          #set terminal node to leaf of child subtree                
            bestVal = max(val,bestVal)                                                  #update bestVal to higher value
            if(bestVal>=beta and i%2==0):                                               #if returned value is greater than beta, then no need to explore right subtree
                print("Pruning max ",node.getRightChild().getNodeId())    
                break                                                                   #prune other child
            alpha = max(alpha,bestVal)                                                  #update alpha to higher value
            
        return bestVal,retNode
    else:
        bestVal = float("inf")                                                          #set initial value to +infinity
        for i in range(0,2):                                                            #loop through children
            if(i%2==0):
                val,leaf = ab_pruning(node.getLeftChild(), depth+1, "Max", alpha, beta) #left child first
            else:
                val,leaf = ab_pruning(node.getRightChild(), depth+1, "Max", alpha, beta) #right child second
            if(val<bestVal):                                                             #if value of child is less than current bestVal
                retNode = leaf                                                           #set terminal node to leaf od child subtree 
            bestVal = min(bestVal,val)                                                  #update bestVal to lesser of itself and returned val
            if(bestVal<=alpha and i%2==0):                                              #if returned value is less than alpha, then no need to explore right subtree
                print("Pruning min ",node.getRightChild().getNodeId())   
                break                                                                   #prune other child
            beta = min(bestVal,beta)                                                    #update beta to lesser of itself and bestVal
            
        return bestVal,retNode                                                          #return best value of node and terminal node
    

'''

Build Tree

'''
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

'''

Call solution functions

'''


print("Minimax Q3.1\n")

print("Output Path:- ")
output = value(tree,"Max")
print()
print("Output Value:- ")
print(output.getNodeValue(),"\n")


print("-------------------------------------------------------------------------")


print("Alpha Beta Pruning Q3.3\n")
bestVal,retNode = ab_pruning(tree, 0, "Max", float("-inf"), float("inf"))
print()
print("Output:-")
print(bestVal)