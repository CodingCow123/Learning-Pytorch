import torch

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0, requires_grad=True)

y_hat = x *w

loss = (y_hat-y)**2
loss.backward()

# print(w.grad)

with torch.no_grad():
    w -= 0.01*loss

w.grad.zero_()
