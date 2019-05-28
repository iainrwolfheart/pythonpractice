mult=int(input("Which times table shall we look at? "))
upto=int(input("How far up shall we go?" ))
a=1
while a<=upto:
	print(mult,"x",a,"=",(mult*a))
	a=a+1
