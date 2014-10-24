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
		self._gameBoard = [[0 for x in xrange(3)] for x in xrange(3)]

		  
