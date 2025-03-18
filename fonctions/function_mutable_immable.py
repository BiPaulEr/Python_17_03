def function(a, liste):
    a = 99
    liste.append(99)
    print("ds la function : ", a)
    return a

a = -1
liste = [1, 2, 3]
a = function(a, liste)
print("hors la function : ", a)
print(liste) #[1, 2, 3, 99]
