def fonction(a, b, *args):
    print(a, b, args)

fonction(1, 2) #1 2 ()
fonction(1, 2, 3) #1 2 (3,)
fonction(1, 2, 3, 4) #1 2 (3, 4)
fonction(1, 2, 3, 4, 5) #1 2 (3, 4, 5)
fonction(1, 2, 3, 4, 5, 6) #1 2 (3, 4, 5, 6)

def maximum(a, b, *args):
    maximum_value = a
    if b > a:
        maximum_value = b
    for element in args:
        if element > maximum_value:
            maximum_value = element
    return maximum_value

print(maximum(1, 6, 9, 10, 11))