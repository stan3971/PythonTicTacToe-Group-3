#!/usr/bin/python3
##########################################
# File Name:main.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:to run the game
########################################

from game import *



def main() :
	gameQuit = False
	
	"""
	testGame = game()
	testGame.nameUser()
	print("")
	testGame.printUserData()
	print("")
	testGame.nameOpponent()
	print("")
	testGame.printOpponentData()
	print("")
	testGame.draw()
	testGame.getMove()
	testGame.draw()
	testGame.resetGame()
	testGame.draw()
	"""
	
	
	
	Game = game()
	Game.nameUser()
	print("")
	Game.printUserData()
	print("")
	Game.nameOpponent()
	print("")
	Game.printOpponentData()
	print("")
	Game.draw()
	
	while not gameQuit :
		
		while Game.gameRunning() :
			Game.getMove()
			Game.draw()
		
		print()
		Game.printUserData()
		
		print("Continue playing (Yes or No)? : Y or N")
		choice = input (">>> ")
		while ( (choice != "Y") and (choice != "N") ) : 
			print ("Y or N?")
			choice = input(">>> ")
			
		if choice == "Y" :
			gameQuit = False
			Game.resetGame()
		else :
			gameQuit = True




if __name__=="__main__" :
	main()



"""
main()


	initialize the game
	get user
	get opponent
	
	quit = False
	
	while (!quit)
	
		while (game running)
			draw()
			game.getMove()
			game.getMove()
			
			
			




"""
