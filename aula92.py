# Yield from
# Basicamente o yield from pega o ultimo retorno da função declarada e faz a continuação dentro de outra função

def gen1(gen=None):
    yield 1
    yield 2
    yield 3

def gen2(gen=None):
    yield from gen()
    yield 4
    yield 5
    yield 6

def gen3(gen=None):
    # yield from gen()
    yield 7
    yield 8
    yield 9

genenerator1 = gen2(gen1)
genenerator2 = gen3(gen2)
genenerator3 = gen2()

for n in genenerator1:
    print(n)
print()
for n in genenerator2:
    print(n)
print()
for n in genenerator3:
    print(n)