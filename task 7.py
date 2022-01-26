from itertools import product

def bar(pr, acc):
    for com in pr:
        if com == "1":
            acc += 1
        elif com == "2":
            acc *= 2
    return acc

def pilot(s, f, l):
    for i in range(1, l + 1):
        space = ["12"] * l
        for j in product(*space):
            pr = "".join(j)
            result = bar(pr, s)
            c = 0
            if result == f:
                c += 1
                return c
    return None

if __name__ == '__main__':
    pr = pilot(1, 16, 15)
    if pr != None:
        print(pr)