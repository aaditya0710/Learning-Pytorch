# -*- coding: utf-8 -*-
"""Understanding-Pytorch-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kb6fSw5PJwGNW2Umh-re5x8Jse0kQoD2
"""

!pip install torch

import torch

torch.__version__

import numpy as np

lst = [3,4,5,6]
lst_num = np.array(lst)

"""Coverting numpy to Pytorch tensors"""

tensors = torch.from_numpy(lst_num)
tensors

tensors[0:2]

tensors[3] = 100

arr = lst_num

tensor_arr = torch.tensor(arr)
tensor_arr

tensor_arr[0] = 10000
print(arr)
print(tensor_arr)

torch.zeros(2,3,dtype=torch.float64)

torch.ones(3,4,dtype=torch.float64)

"""Arithematic operation"""

a = torch.tensor([3,4,5],dtype=torch.float64)
b = torch.tensor([7,8,9],dtype=torch.float64)

a+b

c = torch.zeros(3)

torch.add(a,b,out=c)

torch.add(a,b).sum()

x = torch.tensor([3,4,5],dtype=torch.float)
y = torch.tensor([4,5,6],dtype=torch.float)

x.mul(y)

x.dot(y)

x = torch.tensor([[3,4],[4,6]],dtype=torch.float)
y = torch.tensor([[3,5],[4,5]],dtype=torch.float)

torch.matmul(x,y)

torch.mm(x,y)

x@y

