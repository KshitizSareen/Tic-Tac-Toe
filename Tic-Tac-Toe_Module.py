'''
Created on 06-Nov-2018

@author: hp
'''
import random
from array import *
import string
class TicTacToe:
    Boxes=0 #The number of boxes filled in the 3 by 3 matrix
    variable=0 #The player Vairable
    AI=0 # The AI Variable
    Column=0 
    Result=None
    FirstChance=random.randint(0,1)
    ArrayVar=[]
    ArrayAI=[]
    Matrix=[[None,None,None],[None,None,None],[None,None,None]] # The Matrix to be filled
    Fill=[[False,False,False],[False,False,False],[False,False,False]] # Boolean Matrix to determie if a box is already filled
    def UI(self):
        print "welcome to Tic-Tac-Toe \n"
    
    def ChooseInput(self):
        print "Please press 1 for X \nPlease press 2 for O"
        while(1):
            Input=raw_input() #Input for the player to choose X or O
            if(Input=='1'): #Player Chose X,AI Chose O
                self.variable='X'
                self.AI='O'
                print self.variable
                break
            elif(Input=='2'):#Player Chose O,AI Chose X
               self.variable='O'
               self.AI='X'
               print self.variable
               break
            else:
               print "Please Press 1 or 2 \n"
        self.ArrayVar=[self.variable,self.variable,self.variable]
        self.ArrayAI=[self.AI,self.AI,self.AI]
    def FillMatrix(self):
        if(self.FirstChance==0):# If the first chance is the player chance
            while(1):
                print "Please enter the position you want to place your variable \n"
                print "Please enter the row between 1 and 3 \n"
                while(1):
                    self.row=int(raw_input())# Entering the row of the position the player wants to fill the box
                    if(self.row>=1 and self.row<=3):
                        self.row-=1
                        break
                    else:
                        print "Please enter the row between 1 and 3 \n"
                print "Please enter the column between 1 and 3 \n"
                while(1):
                    self.Column=int(raw_input())# Entering the Column of the position the player wants to fill the box
                    if(self.Column>=1 and self.Column<=3):
                        self.Column-=1
                        break
                    else:
                        print "Please enter the Column between 1 and 3 \n"
                if(self.Fill[self.row][self.Column]==True):
                    print "Please enter a different position \n"
                    continue
                else:
                    self.Matrix[self.row][self.Column]=self.variable #Filling the box with the variable
                    self.Fill[self.row][self.Column]=True #Declairng that box has been filled and cannot be filled again
                    self.FirstChance=1 #Changing the player chance to AI
                    break
        else:
          while(1):
            self.row=random.randint(0,2)# Entering the row of the position the AI wants to fill the box
            self.Column=random.randint(0,2)# Entering the Column of the position the AI wants to fill the box
            if(self.Fill[self.row][self.Column]==True):
                    continue
            else:
                self.Matrix[self.row][self.Column]=self.AI#Filling the box with the variable
                self.Fill[self.row][self.Column]=True#Declairng that box has been filled and cannot be filled again
                self.FirstChance=0#Changing the AI chance to player
                break
        self.Boxes+=1 #Incrementing each box as it has been filled
        self.Result=self.Output() # Printing the ouput of each box
        if(self.Result==0 or self.Result==1 or self.Result==2):
            return
        self.FillMatrix()
    def Output(self):
        a=0
        b=0
        for i in range(3):
            print self.Matrix[i] #Printing the Matrix
        print "\n" 
        if(self.Matrix[0][2]==self.variable and self.Matrix[1][1]==self.variable and self.Matrix[2][0]==self.variable): 
            return 1 #Checking if a combination has been filled and the player has won the game
        elif(self.Matrix[0][2]==self.AI and self.Matrix[1][1]==self.AI and self.Matrix[2][0]==self.AI):
            return 0 #Checking if a combination has been filled and the AI has won the game
               
        for j in range(3):
            if(self.Matrix[j]==self.ArrayVar):
                a+=1
                if(a==1):
                    return 1 #Checking if a row has been filled and the player has won the game
            elif(self.Matrix[j]==self.ArrayAI):
                b+=1
                if(b==1):
                    return 0 #Checking if a row has been filled and the AI has won the game
        a=0
        b=0
        for k in range(3):
            if([row[k] for row in self.Matrix]==self.ArrayVar):
                a+=1
                if(a==1):
                    return 1 #Checking if a Column has been filled and the player has won the game
            elif([row[k] for row in self.Matrix]==self.ArrayAI):
                b+=1
                if(b==1): 
                    return 0 #Checking if a Column has been filled and the AI has won the game
        a=0
        b=0
        for l in range(3):
            if(self.Matrix[l][l]==self.variable):
                a+=1 
                if(a==3):
                    return 1 #Checking if a combination has been filled and the player has won the game
            elif(self.Matrix[l][l]==self.AI):
                b+=1
                if(b==3):
                    return 0 #Checking if a combination has been filled and the AI has won the game
        if(self.Boxes==9):
            return 2 #Checking if all the boxes have been filled and no one has won the game
        
Game=TicTacToe()
Game.UI()
Game.ChooseInput()
Game.FillMatrix()
if(Game.Result==0):
    print "The AI won"
elif(Game.Result==2):
    print "Game Over"
else:
    print "You won"
