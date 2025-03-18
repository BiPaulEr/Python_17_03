def calculer_statistiques(*args, operation=None):
    if not operation:
        return "operation need to be defined"
    elif operation == "somme":
        return sum(args)
    else:
        return sum(args) / len(args) if args else 0

print(calculer_statistiques(2 ,3))
print(calculer_statistiques(3, 2, 5, 8))
print(calculer_statistiques(3, 2, 5, 8, operation="somme"))
print(calculer_statistiques(3, 2, 5, 8, operation="moyenne"))

print(calculer_statistiques(operation="moyenne"))