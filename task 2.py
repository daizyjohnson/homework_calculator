from itertools import product

def boeing(pr, value):
    acc = value
    for command in pr:
        if command == "1":
            acc **= 2
        elif command == "2":
            acc -= 1
    return acc

def pilot(s, f, l):
    for i in range(1, l+1):
        space = ["12"] * l
    for j in product(*space):
        pr = "".join(j)
        result = boeing(pr, s)
        if result == f:
            return pr
    return None

if __name__ == "__main__":
    pr = pilot(5, 8, 4)
    if pr is None:
        print("hy")
    else:
        print(pr)