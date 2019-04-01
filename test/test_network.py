from snn.network import Network
from snn.network import Connection
from snn.network import Layer


class TestNetwork:
    def test_add_layer(self):
        network = Network()
        layer = Layer()
        network.add_layer(layer, "layer_1")

        assert network.layers["layer_1"] == layer
        assert layer.network == network

    def test_add_connection(self):
        network = Network()
        source = Layer()
        target = Layer()
        connection = Connection(source, target)
        network.add_connection(connection, "source", "target")

        assert network.connections[("source", "target")] == connection
        assert connection.network == network
