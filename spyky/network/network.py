import numpy as np
from typing import Dict, NoReturn
from spyky.network import AbstractConnection
from spyky.network.layer import AbstractLayer


class AbstractProbe:
    pass


class Network:
    def __init__(self, dt: float = 1.0) -> NoReturn:
        self.dt = dt
        self.layers = {}
        self.connections = {}
        self.probes = {}

    def add_layer(self, layer: AbstractLayer, name: str) -> NoReturn:
        self.layers[name] = layer
        layer.network = self
        layer.dt = self.dt

    def add_connection(
        self, connection: AbstractConnection, source: str, target: str
    ) -> NoReturn:
        self.connections[(source, target)] = connection
        connection.network = self
        connection.dt = self.dt

    def add_probe(self, probe: AbstractProbe, name: str) -> NoReturn:
        self.probes[name] = probe
        probe.network = self
        probe.dt = self.dt

    def run(
        self, inpts: Dict[str, np.array], time: int = 100, **kwargs
    ) -> NoReturn:
        clamps = kwargs.get("clamp", {})
        unclamps = kwargs.get("unclamp", {})
        masks = kwargs.get("masks", {})
        injects_v = kwargs.get("injects_v", {})

        timesteps = int(time / self.dt)

        inpts.update(self.get_inputs())

        for t in range(timesteps):
            for l in self.layers:
                if isinstance(self.layers[l], AbstractInput):
                    self.layers[l].forward(x=inpts[l][t])
                else:
                    self.layers[l].forward(x=inpts[l])

                clamp = clamps.get(l, None)
                if clamp is not None:
                    if clamp.ndimension() == 1:
                        self.layers[l].s[clamp] = 1
                    else:
                        self.layers[l].s[clamp[t]] = 1

                unclamp = unclamps.get(l, None)
                if unclamp is not None:
                    if unclamp.ndimension() == 1:
                        self.layers[l].s[unclamp] = 0
                    else:
                        self.layers[l].s[unclamp[t]] = 0

                inject_v = injects_v.get(l, None)
                if inject_v is not None:
                    self.layers[l].v += inject_v

            for c in self.connections:
                self.connections[c].update(
                    mask=masks.get(c, None), learning=self.learning, **kwargs
                )

            inpts.update(self.get_inputs())

            for m in self.monitors:
                self.monitors[m].record()

        for c in self.connections:
            self.connections[c].normalize()
