print(list(range(20, 26, 1)))

for number in range(20, 26, 1):
    print(number ** 2)

somme = 0
for number in range(1, 51, 1):
    if number % 2:
        somme = somme + number

print(somme)

somme = 0
for number in range(1, 51, 2):
    somme = somme + number
print(somme)

print(sum(range(1, 51, 2)))