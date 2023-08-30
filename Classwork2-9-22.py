lista = ['a', 'b', 'c', 1, 2, 3, ['x', 'y', 'z']]
listb = [['a', 'b'], 'c', 1, [2, 3, ['x', 'y'], 'z']]


def samethings(lista, listb):
    result = False
    for x in lista:
        for y in listb:
            if x == y:
                result = true
        return result
    return result


print(samethings(lista, listb))
