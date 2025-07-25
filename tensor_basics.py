import torch
import numpy as np

#Creates a new tensor by allocating uninitialized memory for a tensor of the specified shape and data type
# x = torch.empty(2,2,3)

# Creates a tensor with specified dimensions with random values
# x=torch.rand(2,2)

#Create tensors of specified dimensions and fills them with either zeros or ones respectively.
#Can specify data type as a seperate parameter.

# x=torch.zeros(2,2)
# x=torch.ones(2,2, #dtype=torch.int)

# Prints data type of the given tensor
# print(x.dtype)

#Prints size of tensor
#print(x.size())

#How to create a tensor from a list
# x = torch.tensor([2.5,0.1])

# x = torch.rand(2,2)
# y=torch.rand(2,2)
# print(x)
# print(y)

# Both work for element wise addition of tensors
# z=x+y
# z=torch.add(x,y)
# print(z)

# Every function in pytorch with _ will do an inplace operation
# y.add_(x)


# z=x-y
# z=torch.sub(x,y)

# z = x*y
# z= torch.mul(x,y)

# z = x/y
# z=torch.div(x,y)

# Slicing is same as in NumPy
# x = torch.rand(5,3)
# print(x)
# print(x[:, 0])

#.item() gets actual value of a single tensor

#Resize tensors
# x=torch.rand(4,4)
# print(x)
# y=x.view(-1,8)
# print(y)

# a = torch.ones(5)
# print(a)
# b=a.numpy()
# print(type(b))

#If both NumPy and PyTorch are on CPU then changing one created from .numpy() will change the other

#Converting from numpy to torch
# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)

