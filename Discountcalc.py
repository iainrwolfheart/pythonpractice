shop=float(input("How much did your shop come to? £"))
if shop >=50:
	code=input("And what is your discount code? ")
	if code=="jazzmaster" and shop >=100:
		total=shop*0.7
		print("Your total to pay is £",total)
	if code=="strat" and shop >=100:
		total=shop*0.75
		print("Your total to pay is £",total)
	if code=="jazzmaster" and shop in range(50, 99):
		total=shop*0.80
		print("Your total to pay is £",total)
	if code=="strat" and shop in range(50, 99):
		total=shop*0.85
		print("Your total to pay is £",total) 
else: 
	print("You'll have to spend a little more, moneybags.")
