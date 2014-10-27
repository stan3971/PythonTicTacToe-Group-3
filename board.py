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
		self._turns = 0
	
	def printBoard(self) :
		print("  1 2 3 x")
		for x in range(0,3) :
			print (x + 1, end=" ")
			for y in range (0,3) :
				print(self._gameBoard[x][y], end=" ")
			print()
		print("y")
		
	def insertMove(self, move, symbal) :
		if (self.spotTaken(move) == False) :
			self._gameBoard[move.y - 1][move.x - 1] = symbal
			self._turns += 1
		else :
			print("That space is taken")
		
	def reset (self) :
		self.__init__
		
	def checkForWin (self, player) :
		winner = False
		for x in range(0,3) :
			count1 = 0
			count2 = 0
			count3 = 0
			count4 = 0
			for y in range(0,3) :
				if (self._gameBoard[x][y] == player) :
					count1 += 1
				if (self._gameBoard[y][x] == player) :
					count2 += 1
				if (self._gameBoard[2-x][x] == player) :
					count3 += 1
				if (self._gameBoard[y][y] == player) :
					count4 += 1
			if (count1 == 3 or count2 == 3 or count3 ==3 or count4 ==3):
				winner = True
		return winner
		
	def spotTaken (self, move) :
		taken = False
		if ('*' != self._gameBoard[move.y -1][move.x -1]) :
			taken = True
		return taken
		
	def checkForTwo (self) :
		pass
		
	def checkForEmpty (self) :
		empty = True
		if (self._turns != 0) :
			empty = False
		return empty
		
	def checkForFull (self) :
		full = False
		if (self._turns == 9) :
			full = True
		return full
		
#Testing crap
Tic = Board()
move = Point(1,1)
Tic.insertMove(move,'X')
print(Tic.spotTaken(move))
Tic.insertMove(move,'X')
Tic.printBoard()
Tic.printBoard()
print(Tic.checkForWin('X'))
Tic.__init__ ()
Tic.printBoard ()
print(Tic.checkForWin('X'))
print(Tic.spotTaken(move))
