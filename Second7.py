no=int(input("Input number"))
if no>1000:
	print("That's a lot")
	if no>=2000:
		print("... REALLY a lot!")
	else:
		print("... but not REALLY a lot")
	print("Congratulations")
else:
	print("Not much then...")
	if no>=500:
		print("Oh not so bad")
	else:
		print("Oh dear, you need a new job")
	print("Best of luck, my friend")
print("Thank you for sharing.")
