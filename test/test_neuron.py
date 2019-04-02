from snn.neuron import IFNeuron


class TestIFNeuron:
    def test_reset(self):
        v_rest = -50
        n = IFNeuron(shape=(2, 2), v_rest=v_rest)
        v_before_reset = n.v
        spikes_before_reset = n.spikes
        n.reset()
        assert all(v_before_reset.flatten() == v_rest)
        assert all(n.v.flatten() == v_rest)
        assert all(spikes_before_reset.flatten() == 0)
        assert all(n.spikes.flatten() == 0)
