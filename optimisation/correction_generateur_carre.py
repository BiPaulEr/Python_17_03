def gen_pair(compteur):
    for i in range(0, compteur):
        if not i%2:
            yield i

def gen_pair_V2(compteur):
    for i in range(0, compteur, 2):
        yield i

gen = (x for x in range(0, 10, 2))

for i in gen_pair(10):
    print(i)

for i in gen_pair_V2(10):
    print(i)

for i in gen:
    print(i)