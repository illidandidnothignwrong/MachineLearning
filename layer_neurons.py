#Neuron Layer, wich by definition is a layer of neurons, with the same input but different weights and biases
def neuron_layer(weights,bias):
    inputs = [1,2,3,2.5]
    output = 0
    for i in range(len(inputs)):
        output  += weights[i] * inputs[i]
        if i == len((inputs))-1:
            output += bias
            return output
outputs = []
weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5
outputs.append(neuron_layer(weights1,bias1))
outputs.append(neuron_layer(weights2,bias2))
outputs.append(neuron_layer(weights3,bias3))
print(outputs)


