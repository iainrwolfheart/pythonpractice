price=int(input("How much is the bill?"))
paid=int(input("How much money is given?"))
change=paid-price
fifty=change//50
twenty=change%50//20
ten=change%50%20//10
five=change%50%20%10//5
two=change%50%20%10%5//2
one=change%50%20%10%5%2//1
print("The breakdown of change is as follows..;")
if fifty>0:
	print("£50 notes -",fifty)
if twenty>0:
	print("£20 notes -",twenty)
if ten>0:
	print("£10 notes -",ten)
if five>0:
	print("£5 notes -",five)
if two>0:
	print("£2 coins -",two)
if one>0:
	print("£1 coins -",one)
