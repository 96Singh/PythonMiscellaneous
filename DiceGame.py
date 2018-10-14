#!/usr/bin/python
#DiceGuessingGame
#Simple and fun dice game.

from random import randint
result = (randint(1, 6))
guess = input('Guess which number the dice lands on???: ')
try:
	if int(guess) == result:
		print('Yep, you guessed right!')
	else:
		while int(guess) != result:
			print('Sorry, the value you guessed is wrong!\n')
			guess = input('Guess which number the dice lands on???: ')
			if int(guess) == result:
				print('Yep, you guessed right!')
				break
except:
	print("\nValue entered must be a number")
	print('Please enter a number the next time the game is played.')
	print('Game now terminating')
	print('Thank you for playing')