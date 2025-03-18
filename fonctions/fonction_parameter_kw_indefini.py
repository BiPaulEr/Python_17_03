def fonction(a = 2, b = 3, **kwargs):
    print(a, b, kwargs)

fonction() # 2 3 {}
fonction(a = 5) # 5 3 {}
fonction(b = 99) # 2 99 {}

fonction(c = 100) # 2 3 {'c': 100}
fonction(c = 100, d = -2, e = "OK") # 2 3 {'c': 100, 'd': -2, 'e': 'OK'}

fonction(b = 4, o = "OK") #2 4 {"o" : "OK"}

dictionnaire = {'c': 100, 'd': -2, 'e': 'OK'}

fonction(dictionnaire) #{'c': 100, 'd': -2, 'e': 'OK'} 3 {}
fonction(c= 100, d= -2, e= 'OK')
fonction(**dictionnaire)