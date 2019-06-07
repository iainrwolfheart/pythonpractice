write=input("Write a paragraph or two here")
word=input("Which word are we deleting duplicates?")

i=0
first=""
send=""
for i in write:
	if write[i:i+len(word)]==word:
		if first=="":
			first+=word
			send+=word
		else:
			send+=write[i]
	else:
		send+=write[i]
print(send)