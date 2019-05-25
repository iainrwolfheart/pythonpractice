name=(input("What is your name?"))
sal=int(input("What's your salary?"))
ni=sal/100*12
if sal>=50000:
	tax=sal/100*40
if sal in range(30000, 49999):
	tax=sal/100*25
if sal in range(12500, 29999):
	tax=sal/100*20
if sal<12500:
	tax=0
print("Name:",name)
print("Salary:",sal)
print("N.I.:",ni)
print("Tax:",tax)
print("Net Sal:",sal-ni-tax)
