#Implementation of a single Neuron
import numpy as np 
def single_neuron(inputs,weights,bias):
    output = 0
    for i in range(len(inputs)):
        output  += weights[i] * inputs[i]
        if i == len((inputs))-1:
            output += bias
            return output

inputs = [1,2,3]
weights = [0.2,0.8,-0.5]
bias = 2

print(single_neuron(inputs,weights,bias))
inputs2 = [1,2,3,2.5]
weights2 = [0.2,0.8,-0.5,1.0]
bias2 =2.0
print(single_neuron(inputs2,weights2,bias2))