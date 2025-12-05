def id_generator():
    current = 0
    while True:
        current += 1
        yield current

id_gen = id_generator()
