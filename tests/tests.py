from mlx_micrograd.engine import Value
from mlx_micrograd.nn import Module, Neuron, Layer, MLP

# BASIC USAGE
a = Value(-4.0)
b = Value(2.0)
c = a + b
d = a * b + b**3
c += c + 1
c += 1 + c + (-a)
d += d * 2 + (b + a).relu()
d += 3 * d + (b - a).relu()
e = c - d
f = e**2
g = f / 2.0
g += 10.0 / f
print(f'{g.data}') # prints array(24.7041, dtype=float32), the outcome of this forward pass
g.backward()
print(f'{a.grad}') # prints array(138.834, dtype=float32), i.e. the numerical value of dg/da
print(f'{b.grad}') # prints array(645.577, dtype=float32), i.e. the numerical value of dg/db

# MLP EXAMPLES
n = Neuron(2)
x = [Value(1.0), Value(-2.0)]
y = n(x)

model = MLP(2, [16, 16, 1]) # 2-layer neural network
print(model)
print("number of parameters", len(model.parameters()))
