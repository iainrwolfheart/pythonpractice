write=input("Write a paragraph or two here")
word=input("Which word are we deleting duplicates?")

i=0
first=""
send=""
for i in write:
	if write(i:i+len(word))==word:
		if first!=word:
			first+=word[i]
			send+=word[i]
		else:
			send+=word[i]
	else:
		send+=word[i]
print(send)