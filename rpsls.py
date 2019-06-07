import random
rps=["rock", "paper", "scissors", "lizard", "spock"]
computer=rps[random.randint(0,4)]
player=input("Choose rock, paper, scissors, lizard or spock - ")
if player==computer:
	print("It's a tie, what are the chances!")
if player=="rock":
	if computer=="paper":
		print(computer," covers ",player, ", unlucky.")
	if computer=="spock":
		print(computer," vaporises ",player, ", ouch!")
	else computer=="scissors" or "lizard":
		print(player," crushes ",computer,", good work!")
if player=="paper":
	if computer=="scissors":
		print(computer," cuts ",player, ", oh dear.")
	if computer=="lizard":
		print(computer," eats ",player, ", nom nom!")
	if computer=="rock":
		print(player," covers ",computer,", good work!")
	else computer=="spock":
		print(player," disproves ",computer,", smart going!")
