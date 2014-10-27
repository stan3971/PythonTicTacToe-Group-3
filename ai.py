#!/usr/bin/python3
##########################################
# File Name:ai.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:A new challenger approuches
########################################

from player import *

"""
The AI Module
"""

class AI (Player):
	"""Superclass for Hard AI and Easy AI includes a name and symbol"""
	
	def __init__ (self, name, symbol) :
		""" Initializes an object of player setting the passed in name
			and name to the player name and player symbol"""
		self._name = name
		self._symbol = symbol
		
	def getName (self) :
		""" returns the name of the player"""
		return self._name	
		
	def getSymbol (self) :
		""" returns the symbol of the player"""
		return self._symbol
		
	def printPlayer (self) :
		""" prints the player information"""
		print ("Player:", self._name, "Symbol:", self._symbol)
		
	def	placement (self) :
		""" placeholder for deciding where to place a symbol in a 
			Tic-Tac-Toe Board """
		pass 

