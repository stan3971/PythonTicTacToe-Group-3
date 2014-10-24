#!/usr/bin/python3
##########################################
# File Name:unittestPlayer.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:Testing the Player class
########################################
"""
Unit tests for the player class
"""
import unittest
from player import *

class TestPlayerFunctions (unittest.TestCase):

	
	def setUp (self) :
		""" setup for the tests to run"""
		self.player = player("Bob", "X")
		
	def tearDown(self) :	
		"""nothing to tear down"""
		pass
		
	def test_getName (self) :
		"""checks that getName actually returns the correct name"""
		self.assertEqual(player.getName(), "Bob")	
			
	def test_getSymbol (self) :
		"""checks that getName actually returns the correct symbol"""
		self.assertEqual(player.getSymbol(), "X")
