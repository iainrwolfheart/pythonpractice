name=input("Enter name:")
sal=int(input("Enter salary:"))
if sal>25000:
	tax=sal/100*25
if sal in range(12500, 25000):
	tax=sal/100*15
if sal<12500:
	tax=0
netsal=sal-tax
print("Name:",name)
print("Salary:",sal)
print("Your tax:",tax)
print("Net salary:",netsal)