## Spiking Neural Network

A Spiking Neural Network (SNN) is a third generation artificial neural network that integrates time into the operating model. Neurons apart of the SNN represent many different types of neurons found in the brain. The difference between a SNN and a standard perceptron network, is that a Neuron in a SNN is only fired when a membrane potential reaches a specific value, called the activation potential.

In this example of training a SNN on the MNIST hand-written digit set, we incorporate a Leaky-Integrate and Fire Neuron (LIF). Each pixel of the input image is normalized and applied to a LIF neuron.

We do 2D convolution on the neurons from twelve kernels to produce a total of twelve feature maps. The hidden layer size is 8,112 connections (26 * 26 * 12). There are a total of 10 output layers (digits 0 - 9). I will implement an inhibitor on the final output layers using a Winner-Take-All (WTA) approach.

### To Run:
```
./data.sh
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
python train.py
```

### To Do:

Now that we have a working SNN / LIF Model. Take a look at section 2. in the PDF and model the neuron and 2d convolution. Need to update membrane potentials.

- [ ] Create the synaptic layer to the 10 output layers
- [ ] Train the data set
- [ ] Test the training data

### Input Image

<img src="https://github.com/jk-/snn-mnist/blob/master/plots/input_image_4.png" width="200">

### Feature Maps:

Because we updated the model, the image is blank!
