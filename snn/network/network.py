from snn.network import AbstractConnection
from snn.network.layer import Layer


class AbstractProbe:
    pass


class Network:
    def __init__(self, dt: float = 1.0) -> None:
        self.dt = {}
        self.layers = {}
        self.connections = {}
        self.probes = {}

    def add_layer(self, layer: Layer, name: str) -> None:
        self.layers[name] = layer
        layer.network = self
        layer.dt = self.dt

    def add_connection(
        self, connection: AbstractConnection, source: str, target: str
    ) -> None:
        self.connections[(source, target)] = connection
        connection.network = self
        connection.dt = self.dt

    def add_probe(self, probe: AbstractProbe, name: str) -> None:
        self.probes[name] = probe
        probe.network = self
        probe.dt = self.dt
