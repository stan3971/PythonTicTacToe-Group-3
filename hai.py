#!/usr/bin/python3
##########################################
# File Name:hai.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:L33T comp
########################################

# inherits from ai

# placement() - hardAI placement - possibly want to initialize the first 
#				couple of moves and then the rest of the moves will try 
#				to block the user from winning (like looking for two 
#				in a row and placing the symbol appropriately)

"""
The Player Module
"""

from random import randrange
from board import *
from player import *

class HAI (player) :
		"""Superclass for user and AI includes a name and symbol"""
	
	def __init__ (self, name, symbol) :
		""" Initializes an object of player setting the passed in name
			and name to the player name and player symbol"""
		self._name = name
		self._symbol = symbol
		
		
	def printAI (self) :
		""" prints the AI information"""
		print ("AI name:", self._name, "Symbol:", self._symbol)
		
	def	placement (self, board) :
		TwoInRowPoint = board.checkForTwo () # check this name and function
		
		if board.IsEmpty () : #check this name and function
			return Point (1, 1)
		elif 0 != TwoInRowPoint and !board.spotTaken (TwoInRowPoint) : 
			return TwoInRowPoint
		else
			point = Point (randrange(3), randrange(3)
			while board.spotTaken (point) :
				point = Point (randrange(3), randrange(3)
			return point
			
			

			
