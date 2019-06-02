biggest=input("Hello my friends and how are you?")

def count(biggest):
	i=0
	word=""
	large=""
	while i<len(biggest):
		if biggest[i]==" ":
			if len(word)>len(large):
				large=word
				word=""
			else:
				word=""
		else:
			word+=biggest[i]
		i+=1
	if len(word)>len(large):
		large=word
	return large

print("The biggest word is",count(biggest))
