msg=input("Write a sentence and I'll repeat: ")
i=0
word=""
while i<len(msg):
	if msg[i]==" ":
		print(word)
		word=""
	else:
		word=word+msg[i]
	i+=1
print(word)