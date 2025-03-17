age  = input("REntrez votre age")
age  = int(age)

if age >= 18:
    print("Majeur")
else:
    print("Mineur")

print("Majeur") if age >= 18 else print("Mineur")