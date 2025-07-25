import torch

# weights = torch.ones(4,requires_grad=True)

# optimizer=torch.optim.SGD(weights, lr=0.01)
# optimizer.step()
# optimizer.zero_grad()

# for epoch in range(3):
#     model_output = (weights*3).sum()

#     model_output.backward()

#     print(weights.grad)

# Before doing next iteration must empty gradients
#     weights.grad.zero_()


# x = torch.randn(3, requires_grad=True)
# print(x)


# 3 ways to tell PyTorch to stop tracking the gradient
# x.requires_grad_(False)
# x.detach()
# with torch.no_grad():

# y = x+2
# print(y)

# z=y*y*2
# z=z.mean()
# print(z)

#Tells PyTorch how much weight to give to each element of z when calculating the gradient with respect to x
# v = torch.tensor([0.1,1.0,0.001], dtype=torch.float32)

#When .backward is given an argument it will multiply the tensor by the wights and then calculate the gradient
# z.backward(v) 

#Calculates gradient of z in respect to x
# z.backward() 
# print(x.grad)