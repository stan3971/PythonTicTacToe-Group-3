#!/usr/bin/python3
##########################################
# File Name:board.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:board of the game
########################################


class Board :
	"""A single game board"""
	
	def __init__(self) :
		self._gameBoard = [[0 for x in range(3)] for x in range(3)]
		for x in range(0,3) :
			for y in range (0,3) :
				self._gameBoard[y][x] = '*'
	
	def printBoard(self) :
		print("  1 2 3 x")
		for x in range(0,3) :
			print (x + 1, end=" ")
			for y in range (0,3) :
				print(self._gameBoard[x][y], end=" ")
			print()
		print("y")
		
	def insertMove(self, x, y, symbal) :
		self._gameBoard[y - 1][x - 1] = symbal
#Testing crap
Tic = Board()
Tic.insertMove(1,2,'X')
Tic.insertMove(3,1,'O')
Tic.printBoard()
