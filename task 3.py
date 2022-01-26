from itertools import product

def boeing(pr, acc):
    for com in pr:
        if com == "1":
            acc += 3
        elif com == "2":
            acc *= 2
    return acc

def pilot(s, f, l):
    for i in range(1, l + 1):
        space = ["12"] * l
        for j in product(*space):
            pr = "".join(j)
            result = boeing(pr, s)
            if result == f:
                return pr
    return None

if __name__ == '__main__':
    pr = pilot(2, 31, 6)
    if pr != None:
        print(pr)
