
# mlx-micrograd

An mlx port of Karpathy's [micrograd](https://github.com/karpathy/micrograd) - a tiny scalar-valued autograd engine with a small PyTorch-like neural network library on top.

<img width="1177" alt="banner" src="https://github.com/Jaykef/mlx_micrograd/assets/11355002/06c38920-816a-43c3-b6ba-295e914a3246">

### Installation

```bash
pip install mlx_micrograd
```

### Example usage

Example showing a number of possible supported operations:

```python
from mlx_micrograd.engine import Value

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
```

### Training a neural net

`demo.ipynb` provides a full demo of training an 2-layer neural network (MLP) binary classifier. 

### Running tests

To run the unit tests cd into tests folder - which has [test_engine.py](https://github.com/Jaykef/mlx_micrograd/blob/main/tests/test_engine.py) that does sanity checks with pytorch's autograd and [tests.py](https://github.com/Jaykef/mlx_micrograd/blob/main/tests/tests.py) which run tests on some supported ops.

```bash
python test_engine.py
```
```bash
python tests.py
```

### License

MIT
