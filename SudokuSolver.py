#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:19:48 2019

@author: andre
"""
    
def solve(board):
    if findEmpty(board):
        rowLoc, colLoc = findEmpty(board)
    else: return True
    
    for x in range(1,10):
        if valid(board,[rowLoc,colLoc],x):
            board[rowLoc][colLoc] = x
            if solve(board):
                return True
            board[rowLoc][colLoc] = 0
    return False

def findEmpty(board):
    #find next empty entry
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 0:
                return [i,j]

def valid(board, pos, num):
    #start by obtaining rows and columns
    row = board[pos[0]]
    column=[]
    for i in board:
        column.append(i[pos[1]])
    boxRow=pos[0]//3
    boxCol=pos[1]//3
    #DEBUG print(boxRow)
    #DEBUG print(boxCol)
    box = [[],[],[]]
    for i in range(0,3):
       box[i]=board[boxRow*3 + i][boxCol*3:boxCol*3+3]
    #check if num already exists
    if(row.__contains__(num)):
        return False
    if(column.__contains__(num)):
        return False
    if(box.__contains__(num)):
        return False
    #insert tested value
    return True
    
def display(board):
    for i in range(len(board)):
        temp = []
        if(i%3==0 and i!=0):
            print("-------------------------------------")
        for j in range(len(board)):
            if(j%3==0 and j!=0):
                temp.append("|")
            temp.append(board[i][j])
        print(temp)
    
sampleBoard = [
        [0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]               
        ]
display(sampleBoard)
print('\n')
print(solve(sampleBoard))
display(sampleBoard)