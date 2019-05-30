from ProcFunc import Tax

salary=int(input("What is your salary? "))
print("Your tax is", Tax(salary))
print("Your net salary is",salary-Tax(salary))