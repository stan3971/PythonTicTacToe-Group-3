#!/usr/bin/python3
##########################################
# File Name:unittestHAI.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:Testing the hard AI class
########################################
"""
Unit tests for the hai class
"""
import unittest
from hai import *
from board import *

class TestHAIFunctions (unittest.TestCase):

	
	def setUp (self) :
		""" setup for the tests to run"""
		self.hard = HAI("Bob", "X")
		
		
	def tearDown(self) :	
		"""nothing to tear down"""
		pass
		
	def test_EmptyBoard (self) :
		"""tests how the AI chooses a symbol in an empty board"""
		board = Board ()
		returnPoint = self.hard.placement (board)
		self.assertEqual (returnPoint.x, 2)
		self.assertEqual (returnPoint.y, 2) 
			
	def test_RandomPlacement (self) :
		"""tests how the AI chooses a symbol when it should be random"""
		board = Board ()
		board.insertMove (Point (1,1), 'X')
		returnPoint = self.hard.placement (board)
		self.assertNotEqual (returnPoint.x, -1)
		self.assertNotEqual (returnPoint.y, -1)
		
	def test_OwnTwoInRowPlacementHorizontal(self) :
		"""tests how the AI chooses a symbol when it has two in a row
			horizontally
		"""
		board = Board ()
		board.insertMove (Point (1,1), 'X')
		board.insertMove (Point (1,2), 'X')
		returnPoint = self.hard.placement (board)
		self.assertEqual (returnPoint.x, 1)
		self.assertEqual (returnPoint.y, 3)
		
	def test_OwnTwoInRowPlacementVertical(self) :
		"""tests how the AI chooses a symbol when it has two in a row
			vertically
		"""
		board = Board ()
		board.insertMove (Point (1,1), 'X')
		board.insertMove (Point (2,1), 'X')
		returnPoint = self.hard.placement (board)
		self.assertEqual (returnPoint.x, 3)
		self.assertEqual (returnPoint.y, 1)
			
	def test_OwnTwoInRowPlacementDiaLR(self) :
		"""tests how the AI chooses a symbol when it has two in a row
			diagonally with the diagonal from left to right
		"""
		board = Board ()
		board.insertMove (Point (1,1), 'X')
		board.insertMove (Point (2,2), 'X')
		returnPoint = self.hard.placement (board)
		self.assertEqual (returnPoint.x, 3)
		self.assertEqual (returnPoint.y, 3)
		
	def test_OwnTwoInRowPlacementDiaRL(self) :
		"""tests how the AI chooses a symbol when it has two in a row
			diagonally with the diagonal from right to left
		"""
		board = Board ()
		board.insertMove (Point (1,3), 'X')
		board.insertMove (Point (2,2), 'X')
		returnPoint = self.hard.placement (board)
		self.assertEqual (returnPoint.x, 3)
		self.assertEqual (returnPoint.y, 1)
			
