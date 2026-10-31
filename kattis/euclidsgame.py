while True:
    a, b = map(int, input().split())
    if a < 1 and b < 1:
        break
    total = 0
    while b != 0 and a != 0:
        if b > a:
            a, b = b, a
        c = a//b
        total += c
        a, b = b, a-(c*b)
    print(("Ollie" if total%2 else "Stan") + " wins")