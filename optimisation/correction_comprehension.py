noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

etudiants = list(zip(noms, scores))
print(etudiants) #[('Alice', 85), ('Bob', 92), ('Charlie', 78)]
etudiants_17 = [(nom, score / 5) for nom, score in etudiants if (score / 5)  >= 17]
print(etudiants_17) #[('Alice', 17.0), ('Bob', 18.4), ('Charlie', 15.6)]

notes = list(map(lambda tuple : tuple[1], etudiants_17))
print(notes) #[17.0, 18.4]
print(sum(notes) / len(notes)) #17.7