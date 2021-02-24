def g(a, b):
    return a - b

def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    t3 = 2*(t0/t1)
    return t0 + 2*t1 + t3*t3

print("R1:", f(5, 2, 5, 0))
print("R2:", f(0, 2, 3, 3))
print("R3:", f(1, 2, 3, 3))