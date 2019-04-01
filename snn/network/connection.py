import numpy as np

from abc import ABC, abstractmethod
from snn.network.layer import Layer


class AbstractConnection(ABC):
    def __init__(self, source: Layer, target: Layer, **kwargs) -> None:
        assert isinstance(source, Layer), "Source is not of type snn.Layer"
        assert isinstance(target, Layer), "Target is not of type snn.Layer"

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

        if self.weights is None:
            if self.weight_min == -np.inf or self.weight_max == np.inf:
                self.weights = np.clip(
                    np.random.random(
                        (source.neuron_count, target.neuron_count)
                    ),
                    self.weight_min,
                    self.weight_max,
                )
            else:
                self.weights = self.weights_min + np.random.random(
                    (source.neuron_count, target.neuron_count)
                ) * (self.weight_max - self.weight_min)
        else:
            if self.weight_min != -np.inf or self.weight_max != np.inf:
                self.weights = np.clip(
                    self.weights, self.weight_min, self.weight_max
                )

    def calculate(self, spikes: np.array) -> np.array:
        weights_calc = spikes.astype(float) @ self.weights + self.bias
        return weights_calc

    def update(self) -> None:
        pass

    def reset(self) -> None:
        pass
