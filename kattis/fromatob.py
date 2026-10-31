a, b = map(int, input().split())
if a < b:
    print(b-a)
else:
    op = 0
    while a > b:
        if a%2:
            a += 1
        else:
            a //= 2
        op += 1
    print(op + (b-a))