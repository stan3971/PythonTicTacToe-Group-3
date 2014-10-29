#!/usr/bin/python3
##########################################
# File Name:eai.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:NOOB comp
########################################

"""
The EAI Module
"""

from player import *
from random import randrange
from board import *

class EAI (player):
	def __init__(self, name, symbol) :
		player.__init__(self, name, symbol)
		
	def printAI (self) :
		""" prints the AI information"""
		print ("Easy AI name:", self._name)
		print ("Symbol:", self._symbol)
		
	def	placement (self, board) :
		"""This function decides how the AI will choose which point
		to place its symbol. The AI places its symbol randomly.
		"""
		point = Point (randrange(3) + 1, randrange(3) + 1)
		taken = board.spotTaken (point)
		while taken :
			point = Point (randrange(3) + 1, randrange(3) + 1)
			taken = board.spotTaken (point)
		return point
	
