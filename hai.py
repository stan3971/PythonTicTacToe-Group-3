#!/usr/bin/python3
##########################################
# File Name:hai.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:L33T comp
########################################

"""
The HAI Module
"""

from random import randrange
from board import *
from player import *

class HAI (player) :

	def __init__ (self, name, symbol) :
		self._name = name
		self._symbol = symbol
		
		
	def printAI (self) :
		""" prints the AI information"""
		print ("Hard AI name:", self._name)
		print ("Symbol:", self._symbol)
		
	def placement (self, board) :
		"""This function decides how the AI will choose which point
		to place its symbol. If the board is empty it will place it
		in the middle. If the board is not empty it will check for 
		two in a row of its own symbol and place it there otherwise 
		block the enemy's two in a row. Finally it will place a random.
		"""
		badPoint = Point (-1, -1)
		OwnTwoInRow	= board.checkTwoInRow (self._symbol)
		if board.isEmpty () :
			return Point (2, 2)
		else : 			
			if 'X' == self._symbol :
				EnemyTwoInRow = board.checkTwoInRow ('O')
			else :
				EnemyTwoInRow = board.checkTwoInRow ('X')	
		
			if badPoint.x != OwnTwoInRow.x and \
				badPoint.y != OwnTwoInRow.y :
				return OwnTwoInRow
			elif badPoint.x != EnemyTwoInRow.x and \
				 badPoint.y != EnemyTwoInRow.y :
				return EnemyTwoInRow
			else :
				point = Point (randrange(3) + 1, randrange(3) + 1)
				taken = board.spotTaken (point)
				while taken :
					point = Point (randrange(3) + 1, randrange(3) + 1)
					taken = board.spotTaken (point)
				return point		

			
