table = [['']]


def balanceP(n):
    if n < len(table):
        return table[n]

    res = []
    for i in range(n):
        for x in balanceP(i):
            for y in balanceP(n - i - 1):
                res.append('(' + x + ')' + y)

    table.append(res)
    return table[n]

print balanceP(3)