import random

li = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
userScore = 0 
compScore = 0

compChoice = random.choice(li)

print("-" * 50)
print("Welcome to Rock Paper Scissor Lizard Spock")
print("-" * 50)
print('Please use the given format to enter your choice: (enter "Exit" to come out of the game") ', li)
print("")

while (1):
	userChoice = input("Enter your choice: ")
	if userChoice not in li and userChoice!="Exit":
		print('Please input a valid choice ')
	if userChoice==compChoice:
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("It's a DRAW!")
	
	elif userChoice == "Scissors" and compChoice == "Paper":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Scissors cut Paper'")
		userScore += 1

	elif userChoice == "Paper" and compChoice == "Rock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Paper covers Rock'")
		userScore += 1

	elif userChoice == "Rock" and compChoice == "Lizard":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Rock crushes Lizard'")
		userScore += 1

	elif userChoice == "Lizard" and compChoice == "Spock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Lizard poisons Spock'")
		userScore += 1

	elif userChoice == "Spock" and compChoice == "Scissors":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Spock smashes Scissors'")
		userScore += 1

	elif userChoice == "Scissors" and compChoice == "Lizard":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Scissors decapitates Lizard'")
		userScore += 1

	elif userChoice == "Lizard" and compChoice == "Paper":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Lizard eats Paper'")
		userScore += 1

	elif userChoice == "Paper" and compChoice == "Spock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Paper disproves Spock'")
		userScore += 1

	elif userChoice == "Spock" and compChoice == "Rock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Spock vaporizes Rock'")
		userScore += 1

	elif userChoice == "Rock" and compChoice == "Scissors":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("You Win!! as 'Rock crushes Scissors'")
		userScore += 1
		
	elif compChoice == "Scissors" and userChoice == "Paper":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Scissors cut Paper'")
		compScore += 1

	elif compChoice == "Paper" and userChoice == "Rock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Paper covers Rock'")
		compScore += 1

	elif compChoice == "Rock" and userChoice == "Lizard":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Rock crushes Lizard'")
		compScore += 1

	elif compChoice == "Lizard" and userChoice == "Spock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Lizard poisons Spock'")
		compScore += 1

	elif compChoice == "Spock" and userChoice == "Scissors":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Spock smashes Scissors'")
		compScore += 1

	elif compChoice == "Scissors" and userChoice == "Lizard":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Scissors decapitates Lizard'")
		compScore += 1

	elif compChoice == "Lizard" and userChoice == "Paper":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Lizard eats Paper'")
		compScore += 1

	elif compChoice == "Paper" and userChoice == "Spock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Paper disproves Spock'")
		compScore += 1

	elif compChoice == "Spock" and userChoice == "Rock":
		print("Computer's Choice = ",compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Spock vaporizes Rock'")
		compScore += 1

	elif compChoice == "Rock" and userChoice == "Scissors":
		print("Computer's Choice = ", compChoice)
		print("Your Choice = ", userChoice)
		print("Computer Wins!! as 'Rock crushes Scissors'")
		compScore += 1

	elif userChoice=="Exit":
		print('Your score = ', userScore)
		print('Computer Score = ', compScore)
		print("Thanks for playing")
		exit()
