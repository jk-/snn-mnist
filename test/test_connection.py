import numpy as np

from snn.network import Connection
from snn.network import Layer


class TestConnection:
    def test_calculate(self):
        source = Layer()
        target = Layer()

        weights = np.array([0, 1, 2])
        bias = np.array([1, 1, 1])
        spikes = np.array([0, 1, 0])

        c = Connection(source, target, weights=weights, bias=bias)
        weights_calc = c.calculate(spikes)

        assert all([a == b for a, b in zip(weights_calc, [2.0, 2.0, 2.0])])
