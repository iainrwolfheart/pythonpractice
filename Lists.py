msg=input("I'm going to replace 'am': ")
newmsg=""
word=""
i=0
while i<len(msg):
	if msg[i]==" ":
		if word=="am":
			word=""
			newmsg+=" ABC "
		else:
			newmsg+=word
			word=""
	else:
		word+=msg[i]
	i+=1
print(newmsg)
