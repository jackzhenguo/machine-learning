def generatorfun():
    print('step 1')
    yield(10)
    print('step 2')
    yield 30

    return "Okay"

gen = generatorfun()
while True:
    try:
        print(next(gen))
    except StopIteration as e:
        print("return value: "+ e.value)
        break

