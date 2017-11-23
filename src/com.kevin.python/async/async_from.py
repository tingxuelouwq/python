# yield from


def g1():
    yield from range(5)


def g2():
    for item in range(5):
        yield item


it1 = g1()
for x in it1:
    print(x, end=' ')

print('\n---------')

it2 = g2()
for x in it2:
    print(x, end=' ')

