def binom(n,m):
    b = 1
    for i in range(0,m):
        b = b * (n-i) // (i+1)
    return b

def fib(n):
    a = 0
    b = 1
    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return a

if __name__ == "__main__":
    print(binom(100,50))
    print(fib(200))
