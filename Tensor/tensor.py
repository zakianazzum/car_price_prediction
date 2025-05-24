import math


class Tensor:
    def __init__(self, data, _children=(), _op="", requires_grad=True):
        self.data = data  # The scalar or vector value
        self.grad = 0.0  # Gradient wrt
        self._backward = lambda: None  # Function to backpropagate
        self._prev = set(_children)  # Track previous tensors
        self._op = _op  # Operation name (for debugging)
        self.requires_grad = requires_grad  # Flag to track gradients

    def __repr__(self):
        return f"Tensor (data={self.data}, grad={self.grad})"

    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data + other.data, (self, other), "+")

        def _backward():
            if self.requires_grad:
                self.grad += out.grad
            if other.requires_grad:
                other.grad += out.grad

        out._backward = _backward
        return out

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data * other.data, (self, other), "*")

        def _backward():
            if self.requires_grad:
                self.grad += other.data * out.grad
            if other.requires_grad:
                other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * other**-1

    def __pow__(self, power):
        assert isinstance(power, (int, float)), "Only supports int/float powers."
        out = Tensor(self.data**power, (self,), f"**{power}")

        def _backward():
            if self.requires_grad:
                self.grad += (power * self.data ** (power - 1)) * out.grad

        out._backward = _backward
        return out

    def relu(self):
        out = Tensor(self.data if self.data > 0 else 0, (self,), "ReLU")

        def _backward():
            if self.requires_grad:
                self.grad += (out.data > 0) * out.grad

        out._backward = _backward
        return out

    def tanh(self):
        x = self.data
        t = (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)
        out = Tensor(t, (self,), "tanh")

        def _backward():
            if self.requires_grad:
                self.grad += (1 - t**2) * out.grad

        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()

        def build_topo(t):
            if t not in visited:
                visited.add(t)
                for child in t._prev:
                    build_topo(child)
                topo.append(t)

        build_topo(self)
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()


# a = Tensor(2.0)
# b = Tensor(3.0)
# c = a * b + a**2 - b / a
# d = c.relu()
# d.backward()

# print(f"{a.data},{a.grad}")
# print(f"{b.data},{ b.grad}")
# print(f"{d.data}, {d.grad}")

a = Tensor(2.0)
b = Tensor(3.0)
c = a * b + a**2 - b / a
d = c.relu()
d.backward()

print(f"{a.data}, {a.grad}")
print(f"{b.data}, {b.grad}")
print(f"{d.data}, {d.grad}")
