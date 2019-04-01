import numpy as np

from abc import ABC, abstractmethod
from snn.network.layer import Layer


class AbstractConnection(ABC):
    def __init__(self, source: Layer, target: Layer, **kwargs) -> None:
        assert isinstance(source, Layer), "Source is not of type Layer"
        assert isinstance(target, Layer), "Target is not of type Layer"

        self.source = source
        self.target = target
        self.weights = None

        self.weight_min = kwargs.get("weight_min", -np.inf)
        self.weight_max = kwargs.get("weight_max", np.inf)

    @abstractmethod
    def calculate(self, spikes: np.array) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


class Connection(AbstractConnection):
    def __init__(self, source: Layer, target: Layer, **kwargs) -> None:
        super().__init__(source, target, **kwargs)

        self.weights = kwargs.get("weights", None)
        self.bias = kwargs.get("bias", np.zeros(target.neuron_count))

    def calculate(self, spikes: np.array) -> np.array:
        weights_calc = spikes.astype(float) @ self.weights + self.bias
        return weights_calc

    def update(self) -> None:
        pass

    def reset(self) -> None:
        pass
