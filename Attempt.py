def calc(a):
    if a == 0:
        return 1
    else:
        return a*calc(a-1)


n = int(input())
print(calc(n))
