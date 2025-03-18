def produit_error():
    1/0

try:
    produit_error()
except NameError as ne:
    print("NameError ")
    print(ne)
except ArithmeticError as e:
    print("ArithmeticError ")
    print(e)
except Exception as e:
    print("Exception ")
    print(e)
