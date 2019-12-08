import os
import seaborn as sns
import numpy as np

sns.set()

def create_layers(indata, x, y):
    layers = np.array(indata).reshape(int(len(indata)/(x*y)),y,x)
    l_range,_,_ = layers.shape
    min_layer = 100000
    min_zeros = 100000
    for layer in range(l_range):
        zeros = (layers[layer]==0).sum()
        if zeros < min_zeros:
            min_layer = layer
            min_zeros = zeros

    return (layers[min_layer]==1).sum() * (layers[min_layer]==2).sum()
    
def decode_image(indata, x, y):
    layers = np.array(indata).reshape(int(len(indata)/(x*y)),y,x)
    result = 2 * np.ones((y,x),dtype=int)
    for i in range(y):
        for j in range(x):
            for l in layers[:,i,j]:
                if l != 2:
                    result[i,j] = l
                    break
    heat = sns.heatmap(result,cbar=False, cmap="binary")
    fig = heat.get_figure()
    fig.savefig("assets/8fig.png")
    return result

def solve81(path: str = 'assets/des8.1.txt') -> int:
    with open(path) as fh:
        lines = [line.strip() for line in fh.readlines()]
        data = [int(c) for c in "".join(lines)]
    return create_layers(data, 25, 6)

def solve82(path: str = 'assets/des8.1.txt') -> int:
    with open(path) as fh:
        lines = [line.strip() for line in fh.readlines()]
        data = [int(c) for c in "".join(lines)]
    return decode_image(data, 25, 6)



if __name__ == "__main__":
    print(f"solve 8.1: {solve81()}")
    print(f"solve 8.2: {solve82()}")
