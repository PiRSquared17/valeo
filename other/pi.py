k, a, b, a1, b1 = 2, 4, 1, 12, 4
for i in range(0, 2000):
    p, q, k = k*k, 2*k+1, k+1
    a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
    d = a / b
    d1 = a1 / b1
    while d == d1:
        print d
        a, a1 = 10*(a%b), 10*(a1%b1)
        d, d1 = a/b, a1/b1
