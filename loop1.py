msg=input("Write stuff here")
find=input("Which word shall we look for?")
f=0
m=0
while m<len(msg):
	if msg[m:m+len(find)]==find:
		f=f+1
		m=m+len(find)-1
	m=m+1
print(f)
