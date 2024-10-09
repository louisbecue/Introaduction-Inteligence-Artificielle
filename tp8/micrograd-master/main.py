from micrograd.engine import Value
from graphviz import Digraph

step = 0.01

# quand x = 3y la fonction est minimale

x = Value(3)
y = Value(5)

for i in range(100):
    g = ((x - 3 * y)**2 + 1)
    print(x, y)
    g.backward()
    print("x", x.grad)
    print("y", y.grad)
    x.data -= step*x.grad
    y.data -= step*y.grad
    x.grad, y.grad = 0, 0