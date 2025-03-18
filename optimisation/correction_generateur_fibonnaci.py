def fibonacci():
    yield 0
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b
       
for i in fibonacci():
    print(i)

#0, 1, 1, 2, 3, 5 …