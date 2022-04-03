# 15 Puzzle Solver dengan Algoritma Branch and Bound
# Lyora Felicya / 13520073

import time
import random
import numpy as np

goal = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4) 
direction = ("Up", "Right", "Down", "Left")

class PrioQueue:
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        index = 0
        for i in range(len(self.queue)):
            if(self.queue[i][0] < self.queue[index][0]):
                index = i
        item = self.queue[index]
        del self.queue[index]
        return item

class Node:
    def __init__(self, data=None):
        self.matrix = data
        self.parent = None
        self.move = ""
        self.depth = 0

# find position
def findPosition(x, puzzle):
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == x:
                position = matrix[i][j]
    return position

# Kurang(i) function
def less(i, puzzle):
    # Number of tiles where j < i and position(j) > position(i)
    count = 0
    if (i != 16):
        for row in range(4):
            for col in range(4):
                j = puzzle[row][col]
                j_pos = findPosition(j,puzzle)
                i_pos = findPosition(i,puzzle)
                if (j < i) and (j_pos > i_pos) and (j != 0):
                    count += 1
    else:
        blankSpacePos = findPosition(0,puzzle)
        count = 16 - blankSpacePos
    return count

# get row and col of blank space
def findBlankSpace(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 0):
                row = i
                column = j
    return row,column

# to determine the value of X
def findX(puzzle):
    i, j = findBlankSpace(puzzle)
    if((i+j) % 2 == 1):
        X = 1
    else:
        X = 0
    return X

# print Kurang(i) for each tile
def printLess(puzzle) :
    sum = 0
    X = findX(puzzle)
    print("Fungsi Kurang(i)")
    print("=================================================")
    for i in range(1,17) :
        print("Kurang"+"("+str(i)+")" + " : " + str(less(i, puzzle)))
        sum += less(i, puzzle)
    print()
    print("Total : " + str(sum))
    print("X : " + str(X))
    if((X+sum) % 2 == 0) :
        print("sigma KURANG(i) + X = " + str(X+sum) + " (even)")
    else:
        print("sigma KURANG(i) + X = " + str(X+sum) + " (odd)")

# to determine if the puzzle is solveable
def isSolveable(puzzle):
    sum = 0
    X =  findX(puzzle)
    for i in range(1,17):
        sum = sum + less(i, puzzle)
    sum += X
    if(sum % 2 == 0):
        return True
    else:
        return False

# calculate cost of a node
def cost(depth,matrix,goal):
    misplaced = 0
    for i in range(4):
        for j in range(4):
            # count number of misplaced tiles
            if((matrix[i][j] != goal[i][j]) and matrix[i][j] != 0):
                misplaced += 1
    cost = misplaced + depth
    return cost   

# Functions to Move Puzzle Tiles
def swap(matrix,row,column):
    x,y = findBlankSpace(matrix)
    matrix[x][y] = matrix[row][column]
    matrix[row][column] = 0
    return matrix

def move(matrix,direction):
    matrix_temp = matrix.copy()
    x,y = findBlankSpace(matrix_temp)
    if(direction == "Left"):
        if(y != 0):
            y -= 1
    elif(direction == "Right"):
        if(y != 3):
            y += 1
    elif(direction == "Up"):
        if(x != 0):
            x -= 1
    elif(direction == "Down"):
        if(x != 3):
            x += 1
    matrix_temp = swap(matrix_temp,x,y)
    return matrix_temp

def oppositeDirection(direction):
    if(direction == "Left"):
        return "Right"
    elif(direction == "Right"):
        return "Left"
    elif(direction == "Up"):
        return "Down"
    elif(direction == "Down"):
        return "Up"

# to check if the goal state is reached
def equal(matrix,goal):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != goal[i][j]):
                return False
    return True

# print matrix without brackets
def printMatrix(matrix) :
    for i in range(4) :
        for j in range(4) :
            if (matrix[i][j] < 10) :
                print(str(matrix[i][j]) + " ", end=" ")
            else :
                if (matrix[i][j] == 16) :
                    print("0 ", end=" ")
                else :
                    print(matrix[i][j], end=" ")
        print()

# print nodes from initial state to goal
def printSolution(node):
    if(node.parent == None):
        return
    printSolution(node.parent)
    print()
    print("---------------")
    print("Step "+ str(node.depth) + " : " + str(node.move))
    print("---------------")
    printMatrix(node.matrix)
    print("---------------")

# find solution using Branch and Bound
def solve(puzzle):

    # set initial puzzle state as root node
    node = Node(puzzle)
    Queue = PrioQueue()
    nodeExpanded = 0

    # add root node to queue and calculate root cost
    Queue.enqueue((cost(0,node.matrix,goal),node,"",0))

    # remove root node from queue of livenodes
    liveNodes = Queue.dequeue()

    node = liveNodes[1]
    curNode = node.matrix
    prev = ""
    next_step = liveNodes[3] + 1
    nodeExpanded += 1

    # check if the goal is reached
    while(not equal(curNode, goal)):
        for dir in direction:
            if(dir != prev):
                expandedNode = move(curNode,dir)
                if(not equal(expandedNode, curNode)):
                    # Expand new node
                    newNode = Node(expandedNode)
                    newNode.parent = node
                    newNode.depth = node.depth + 1
                    nodeExpanded += 1
                    newNode.move = dir

                    # Add new expanded node to Queue
                    Queue.enqueue((cost(next_step,newNode.matrix,goal),newNode,dir,next_step))      
        
        liveNodes = Queue.dequeue()
        node = liveNodes[1]
        curNode = node.matrix
        Move = liveNodes[2]
        prev = oppositeDirection(Move)
        next_step = liveNodes[3] + 1

    printSolution(node)
    return nodeExpanded