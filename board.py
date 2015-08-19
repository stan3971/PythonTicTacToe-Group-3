#!/usr/bin/python3
##########################################
# File Name:board.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:board of the game
########################################


class Point:
	
	
	def __init__(self, x, y) :
		self.x = x
		self.y = y

class Board :
	"""A single game board"""
	
	def __init__(self) :
		self._gameBoard = [[0 for x in range(3)] for x in range(3)]
		for x in range(0,3) :
			for y in range (0,3) :
				self._gameBoard[y][x] = '*'
		self._numMoves = 0
	
	def printBoard(self) :
		print("  1 2 3 x")
		for x in range(0,3) :
			print (x + 1, end=" ")
			for y in range (0,3) :
				print(self._gameBoard[x][y], end=" ")
			print()
		print("y")
		
	def insertMove(self, move, symbal) :
		if(self.checkForRange(move) == True) :
			if (self.spotTaken(move) == False) :
				self._gameBoard[move.y - 1][move.x - 1] = symbal
				self._numMoves = self._numMoves + 1
			
				return True
			else :
				return False
		else :
			return False
		
	def reset (self) :
		self.__init__()
				
	def spotTaken (self, move) :
		taken = False
		if ('*' is not self._gameBoard[move.y -1][move.x -1]) :
			taken = True
		return taken
		
	def checkForTwo (self) :
		pass
		
	def isEmpty (self) :
		if (self._numMoves == 0) :
			return True
		else :
			return False
		
	def isFull (self) : 
		if (self._numMoves == 9) :
			return True
		else :
			return False
			
	def checkPoint (self, x, y, symbol) : 
		if self._gameBoard[y][x] == symbol :
			return True
		else :
			return False
			
	def checkWinHorizontal (self, symbol) :
		for y in range (0,3) :
			count = 0
			for x in range (0,3) :
				if self.checkPoint(x,y,symbol) : 
					count = count + 1
			if count == 3 :
				return True
		return False

	def checkWinVertical (self, symbol) :
		for x in range (0,3) :
			count = 0
			for y in range (0,3) :
				if self.checkPoint(x,y,symbol) : 
					count = count + 1
			if count == 3 :
				return True
		return False	
	
	def checkWinDiagonal(self, symbol) : 
		count1 = 0
		count2 = 0
		for value in range(0,3) :
			if self.checkPoint(value, value, symbol) :
				count1 += 1
			if self.checkPoint(value, (2 - value), symbol) :
				count2 += 1
		if count1 == 3 or count2 == 3 :
			return True
		else :
			return False
			
	def checkWin(self, symbol) :
		if (self.checkWinDiagonal(symbol) or \
		self.checkWinHorizontal(symbol) or \
		self.checkWinVertical(symbol)):
			return True
		else :
			return False
			
	def checkForRange (self, move) :
		if (move.y > 0 and move.y < 4 and move.x > 0 and move.x < 4) :
			return True
		else :
			return False
		
		
		
#Testing crap
Tic = Board()
move = Point(4,4)
print(Tic.checkForRange(move))
#Tic.insertMove(move,'X')
#print(Tic.spotTaken(move))
#Tic.insertMove(move,'X')
#Tic.printBoard()
#Tic.printBoard()
#print(Tic.checkForWin('X'))
#Tic.__init__ ()
#Tic.printBoard ()
#print(Tic.checkForWin('X'))
#print(Tic.spotTaken(move))


"""

Tic = Board()
move1 = Point(1,1)
move2 = Point(1,2)
move3 = Point(1,3)


Tic.insertMove(move1, 'X')
Tic.insertMove(move2, 'X')
Tic.insertMove(move3, 'X')
Tic.printBoard()
#print(Tic.checkWinHorizontal ('X'))
#print(Tic.checkWinVertical ('X'))
#print(Tic.checkWinDiagonal ('X'))
print(Tic.checkWin('X'))

"""



