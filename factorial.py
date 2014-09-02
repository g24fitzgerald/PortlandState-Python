def G(n):
    if n==0:
        return 1
    return (n * G(n-1))
print(G(5))



