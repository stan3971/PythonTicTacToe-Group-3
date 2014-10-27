#!/usr/bin/python3
##########################################
# File Name:eai.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:NOOB comp
########################################


from player import *
from random import randrange
from board import *

# inherits from ai

# placement() - easyAI placement - possibly want to set the moves 
#				randomly

class EAI (player):
	def __init__(self, name, symbol) :
		player.__init__(self, name, symbol)
		
	def printAI (self) :
		""" prints the AI information"""
		print ("AI name:", self._name, "Symbol:", self._symbol)
		
	def	placement (self, board) :
		point = Point (randrange(3) + 1, randrange(3) + 1)
		taken = board.spotTaken (point)
		while taken :
			point = Point (randrange(3) + 1, randrange(3) + 1)
			taken = board.spotTaken (point)
		return point
	
