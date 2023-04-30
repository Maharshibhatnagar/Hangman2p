def gamePlay(secretWord): #This line defines a function called gamePlay that takes one argument called secretWord.
	failedGuesses = 0
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	guess = ""
	displayWord = getDisplayWord(secretWord)
	gameOver = False
 
#  These lines initialize some variables that will be used later in the function. failedGuesses keeps track of the number of incorrect guesses, alphabet is a string containing all the uppercase letters of the English alphabet, guess will hold the current guess, displayWord is the current state of the secret word being guessed with underscores for unguessed letters, and gameOver is a boolean variable that will be set to True when the game ends.

	while not gameOver:        #This starts a while loop that will continue until the game is over can also use while we just have to initialize the gameOver with true.
		invalidInput = True
		while invalidInput:
			print("Player", Player, end = "")
			guess = input(", please guess a letter: ").upper()
			if len(guess) > 1 or guess not in alphabet:
				print("You did enter a valid guess. Please try again.")  
			else:
				invalidInput = False   #This code prompts the user to input a letter and validates it. If the input is invalid (more than one character or not in the alphabet), it asks the user to try again.
		if guess in secretWord:
			for i in range(len(secretWord)):
				if secretWord[i] == guess:
					displayWord[i] = guess
			printWord(displayWord)
			if "_" not in displayWord:
				print("Player", Player, " wins!")
				gameOver = True
		else:
			failedGuesses += 1
			print("Your guess is incorrect! Please try again.")
			print("Hangman Status: ", end = "")

			if failedGuesses == 1:
				print("O")
			elif failedGuesses == 2:
				print("O-")
			elif failedGuesses == 3:
				print("O_O")
			elif failedGuesses == 4:
				print("O-<")
			elif failedGuesses == 5:
				print("O+<")
			elif failedGuesses == 6:
				print("You died!")
				gameOver = True
			print("Number of chances left:", 6-failedGuesses)

			printWord(displayWord)   #This code checks if the guessed letter is in the secret word. If it is, it updates displayWord to reveal the guessed letters and checks if the word has been fully guessed. If the word is fully guessed, it prints a message that the player has won and sets gameOver to True. If the guessed letter is not in the secret word, it increments failedGuesses, displays the current state of the hangman drawing, and checks if the player has lost the game. If the player has lost, it prints a message and sets gameOver to True.
							
def printWord(displayWord):
	word = ""
	for i in range(len(displayWord)):
		word += displayWord[i]
	print()
	print("Current Progress: ", word)
#  word = "": Initialize an empty string called word.
# for i in range(len(displayWord)):: Loop over the indices of displayWord.
# word += displayWord[i]: Append the character at the current index of displayWord to the word string.
# print(): Print a newline character to start a new line.
# print("Current Progress: ", word): Print the string "Current Progress: " followed by the word string, which represents the current progress of the word being guessed. 

def getDisplayWord(secretWord):
	displayWord = []
	for i in range(len(secretWord)):
		if secretWord[i] in alphabet:
			displayWord.append("_")
		else:
			displayWord.append(secretWord[i])
	return displayWord

# This function takes in the secretWord and creates a list displayWord of underscores and spaces that represents the current state of the game. It iterates through each letter of the secretWord and appends either an underscore or the letter to the displayWord list. The function returns the displayWord list.

def main():
	global Player
	global alphabet
	Player = 1
	secretWord = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"		
	Continue = True

	while Continue:		
		if Player == 1:
			print()
			secretWord = input("Player one, please enter your secret word: ").upper()
			for i in range(50):
				print()
			Player = 2
			print("Player 2 must guess Player's One's word")
			gamePlay(secretWord)
		elif Player == 2:
			print()
			secretWord = input("Player two, please enter your secret word: ").upper()
			for i in range(50):
				print()
			Player = 1
			print("Player 1 must guess Player's Two's word")
			gamePlay(secretWord)
		quit = input("Do you want to quit? (Yes/No): ").upper()   
		if quit == "YES" or quit == "Y" or quit=='y':
			Continue = False   
#    This code defines a function named `main` which is the entry point for the program. Within the function, two global variables `Player` and `alphabet` are initialized. The variable `Player` is used to keep track of which player is currently playing, and `alphabet` is a string of all uppercase letters of the English alphabet.

# The variable `secretWord` is initialized to an empty string, which is later used to store the secret word entered by the players. The variable `Continue` is initialized to `True` which is used to control the loop that allows players to keep playing the game.

# The while loop runs as long as `Continue` is `True`. Inside the loop, if `Player` is 1, the program asks the first player to enter a secret word. The `input` function is used to prompt the player for input and the input string is converted to uppercase using the `upper()` method. Then, the function `gamePlay` is called with the secret word as an argument. 

# If `Player` is 2, the program asks the second player to enter a secret word in the same way as the first player. Then, the function `gamePlay` is called again with the secret word as an argument. After the game is finished, the program asks if the players want to quit playing the game. 

# The `quit` variable is assigned the input value of whether the player wants to continue playing or not. If the input value is "YES" or "Y" or "y", the `Continue` variable is set to False, which stops the while loop and exits the program. If the input value is anything else, the program continues by looping back to the start of the while loop and asking for the secret word again. Finally, the program prints a message thanking the players for playing the Hangman game.
	print()
	print("Thank you for playing Hangman!")

main()