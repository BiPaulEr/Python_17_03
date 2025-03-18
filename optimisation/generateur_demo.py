chaine = "Bonj"
"""
object_iterable = iter(chaine)

print(next(object_iterable))
print(next(object_iterable))
print(next(object_iterable))
print(next(object_iterable))

print(next(object_iterable)) #StopIteration"
"""
for carac in iter(chaine):
    print(carac)

def generateur(compteur):
    for i in range(0, compteur):
        yield i
        print("OK")

gen = generateur(4)

for i in gen:
    print("1 fois : ", i)

for i in gen:
    print("2e utilisation : ", i)

for i in generateur(18):
    print("Generateur neuf : ", i)
