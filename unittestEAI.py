#!/usr/bin/python3
##########################################
# File Name:	unittestEAI.py
# Author:		Group 3
# Date:			10/28/14
# Class:		360
# Assignment:	Tic-Tac-Toe
# Purpose:		Testing the EAI class
########################################
"""
Unit tests for the EAI class
"""

import unittest
from eai import *

class TestUserFunctions (unittest.TestCase) :
	
	def setUp (self) :
		""" setup for the tests to run """
		self.eai = EAI("Gary", "O")
		self.board = Board()
		
	def tearDown (self) :
		""" nothing to tear down """
		pass
		
	def test_placement (self) :
		""" nothing to tear down """
		self.testpoint = Point(-1,-1)
		self.returnpoint = self.eai.placement(self.board)
		self.assertNotEqual(self.testpoint, self.returnpoint)
		
