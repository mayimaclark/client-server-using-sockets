from polynomials import evaluate, bisection

poly = [-945, 1689, -950, 230, -25, 1]
x = 1.0
a = 0
b = 2
tol = 1e-15

v = evaluate(x, poly)
print(v)

r = bisection(a, b, poly, tol)
print(r)
