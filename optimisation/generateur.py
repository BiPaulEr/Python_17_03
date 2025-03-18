noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
etudiants = list(zip(noms, scores))

etudiants_17 = [(nom, score / 5) for nom, score in etudiants if (score / 5)  >= 17]
print(etudiants_17) #[('Alice', 17.0), ('Bob', 18.4)]

etudiants_17_gen = ((nom, score / 5) for nom, score in etudiants if (score / 5)  >= 17)
print(etudiants_17_gen) #<generator object <genexpr> at 0x0000025CBFDE1D20>
