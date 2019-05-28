import random
rps=["rock", "paper", "scissors"]
computer=rps[random.randint(0,2)]
go="y"
while go=="y":
	player=input("Choose rock, paper or scissors - ")
	if player==computer:
		print("It's a tie!")
	elif player=="rock":
		if computer=="paper":
			print(computer, "beats",player,"so you lose, sucka!")
		else:
			print(player,"beats",computer,"so you win, noice!")
	elif player=="paper":
		if computer=="rock":
			print(player,"beats",computer,"so you win, noice!")
		else:
			print(computer, "beats",player,"so you lose, sucka!")
	elif player=="scissors":
		if computer=="rock":
			print(computer, "beats",player,"so you lose, sucka!")
		else:
			print(player,"beats",computer,"so you win, noice!")
	else:
		print("That's not one of the choices, sadly.")
	go=input("Would you like to play again? y/n - ")
print("Thank you for playing!")
