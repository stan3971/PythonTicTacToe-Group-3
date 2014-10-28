#!/usr/bin/python3
##########################################
# File Name:user.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:player of the game
########################################

# inherits from player
from player import *
from board import *

class user (player): 
	"""Represents a user player"""
	
	def __init__ (self, name, symbol, wins, losses, draws) :
		player.__init__(self, name, symbol)
		self._wins = wins
		self._losses = losses
		self._draws = draws
		
	def getWins (self) :
		return self._wins
		
	def getLosses (self) :
		return self._losses
		
	def getDraws (self) :
		return self._draws
		
	def printData (self) :
		self.printPlayer()
		print ("Wins:", self._wins, "Losses:", self._losses, "Draws:", self._draws)
		
	def placement (self, board) :
		spotTaken = True
		
		while spotTaken : 
			print("")
			print ("X?")
			x = int(input(">>> "))
			while x < 0 and x > 4 : 
				x = int(input(">>> "))
			
			print("Y?")
			y = int(input(">>> "))
			while y < 0 and y > 4 :
				y = int(input(">>> "))
			
			point = Point(x,y)
			spotTaken = board.spotTaken(point)
		
		return Point(x,y)
		#ask for x and y
		
		#check if the spot is taken!!! these are valid (space can be taken and between 1 and 3)
		
		#put coordinates in a point class/object
		#return the point
	def incrementWins(self) :
		self._wins = self._wins + 1

	def incrementLosses(self) :
		self._losses = self._losses + 1
		
	def incrementDraws(self) :
		self._draws = self._draws + 1
		

# printData () - print wins, losses, and draws

# numWins

# numLosses

# numDraws

#testUser = user("Bob", "X", 1, 2, 3)
#testUser.printData()
