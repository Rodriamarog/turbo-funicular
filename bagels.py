import random

NUM_DIGITS = 3
MAX_GUESSES = 15

def main():
	print('''This is going to bet the baegels.py program!

A deductive logic game.
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
When I say:			That means:
  Pico			    One digit is correct but in the wrong position.
  Fermi			    One digit is correct and in the right positoion.
  baegels			No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

	# Main game loop.
	while True:
		# This stores the secret number the player needs to guess:
		secretNum = getSecretNum()
		print('I have thought up a number.')
		print(' You have {} guesses to get it.'.format(MAX_GUESSES))

		numGuesses = 1
		while numGuesses <= MAX_GUESSES:
			guess = ''
			# Keep looping until they enter a valid guess:
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Guess #{} '.format(numGuesses))
				guess = input('> ')

			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1

			if guess == secretNum:
				# They're correct, so break out of this loop.
				break
			if numGuesses > MAX_GUESSES:
				print('You ran out of guesses.')
				print('The answer was {}.'.format(secretNum))

		# Ask player if they want to play again.
		print('Do you want to play again? (yes or no)')
		if not input('> ').lower().startswith('y'):
			break
	print('Thanks for playing!')

def getSecretNum():
	"""Returns a string made up of NUM_DIGITS unique random digits."""
	# Create a list of digits 0 to 9.
	numbers = list('0123456789')
	# Shuffle them into random order.
	random.shuffle(numbers)

	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	"""Returns a string with the pico, fermi, bagels clues for a guess
	and secret number pair."""
	if guess == secretNum:
		return 'You got it!'

	clues = []

	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			# A correct digit is in the right place
			clues.append('Fermi')
		elif guess[i] in secretNum:
			# A correct digit is in the incorrect place.
			clues.append('Pico')
	if len(clues) == 0:
		# There are no correct digits at all.
		return 'Bagels'
	else:
		clues.sort()
		return ''.join(clues)

# If the program is ran (instead of imported), run the game:
if __name__ == '__main__':
	main()

