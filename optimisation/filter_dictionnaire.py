prenoms = {"prenom" : 1, "pol" : 2, "okokokokokokokoko" : 6, "cal" : 8}

items = prenoms.items()
print(list(items))
#[('prenom', 1), ('pol', 2), ('okokokokokokokoko', 6), ('cal', 8)]#

prenoms_true = list(filter(lambda tuple: len(tuple[0]) > 4, items))
print(prenoms_true) #[('prenom', 1), ('okokokokokokokoko', 6)]

dictionnaire = dict(prenoms_true)
print(dictionnaire) #{'prenom': 1, 'okokokokokokokoko': 6}

for key in prenoms.keys():
    if len(key) < 4:
        prenoms.pop(key)