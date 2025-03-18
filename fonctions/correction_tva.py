def calculer_prix_ttc(tva, ht):
    ttc = (1 + tva / 100) * ht
    return ttc

result = calculer_prix_ttc(20, 100)
print(result)
