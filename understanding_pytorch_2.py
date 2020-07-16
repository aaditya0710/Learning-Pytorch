# -*- coding: utf-8 -*-
"""Understanding-Pytorch-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kb6fSw5PJwGNW2Umh-re5x8Jse0kQoD2
"""

import torch

x = torch.tensor(4.0,requires_grad=True)
x

y = x**2
y.backward()

print(x.grad)

l = [[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]]
torch_input = torch.tensor(l,requires_grad=True)

torch_input

y=torch_input**3+torch_input**2

z = y.sum()

z.backward()

torch_input.grad
