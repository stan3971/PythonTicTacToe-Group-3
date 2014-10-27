#!/usr/bin/python3
##########################################
# File Name:game.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:to run the game
########################################


from user import *
from hai import *
from eai import *
from board import *

class game :
	""" the game """
	
	def __init__ (self) :
		self._board = Board()
		self._userFirst = True
		self._gameNum = 0
		self._gameRunning = True
		self._userTurn = True
		
	def nameUser (self) :
		print ("Enter name:")
		name = input(">>> ")
		print ("X or O?")
		symbol = input(">>> ")
		while ((symbol != "X") and (symbol != "O") ) :
			print ("X or O?")
			symbol = input(">>> ")
		
		self._user = user (name, symbol, 0, 0, 0)
		
	def userSymbolIsX (self) : 
		userIsX = False
		if (self._user.getSymbol() == "X" ) :
			userIsX = True
		return userIsX
	
	def printUserData (self) : 
		self._user.printData()
	
	def nameOpponent (self) :
		print ("Enter opponent difficulty (Easy or Hard): E or H?")
		difficulty = input (">>> ")
		while ( (difficulty != "E") and (difficulty != "H") ) : 
			print ("E or H?")
			difficulty = input(">>> ")
		
		print("Enter opponent name: ")
		aiName = input(">>> ")
		
		if (self.userSymbolIsX()) :
			aiSymbol = "O"
		else :
			aiSymbol = "X"
			
		if (difficulty == "E") :
			self._ai = EAI (aiName, aiSymbol)
			
		if (difficulty == "H") :
			self._ai = HAI (aiName, aiSymbol)
			
	def printOpponentData (self) : 
		self._ai.printAI()
		
		
	def getTurn(self) : 
		if (self._userTurn ==  True) :
			return self._user.getSymbol()
		else :
			return self._ai.getSymbol()
			
	def getMove(self) : 
		symbol = self.getTurn()
		
		if (self._userTurn ==  True) :
			self._user.placement(self._board)
			
	
	#def userWin (self) : 
	
	def updateTurn (self, symbol) :
		
		
		
		
		
		
		
		if self._board.isFull() :
			self._gameRunning = False
		
		
	#def resetGame (self) : 
		
		
		
testGame = game()
testGame.nameUser()
testGame.printUserData()
testGame.nameOpponent()
testGame.printOpponentData()

# gameCreate() - initializes the game (user wins, losses, draws = 0, board is empty)...

# userFirst = true/false (something like that)

# gameNum = 0 (start at 0)

# nameUser() - function to prompt the user to enter the name and store this info in user class?

# nameOpponent() - just like nameUser

# userSymbolX = true/false - sets user.symbol and ai.symbol

# aiEasy = true/false - makes ai to hard or easy...

# userWin = true/false type of thing

# gameUpdate() - updates aspects of the game (wins, losses, board)...

# resetGame() - if the user wants to play again, resets the board

# usermove (x,y) - take coordinates of the user moves -> this gives info to board as well
