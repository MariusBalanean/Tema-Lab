def pare(l, r):
    k = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i % 2 == 0 and j % 2 == 0:
                k = k+1
    return k


def main():
    l = int(input())
    r = int(input())
    print(pare(l, r))

main()