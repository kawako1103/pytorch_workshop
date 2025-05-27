import torch, torchvision, torch.nn as nn, torch.optim as optim
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

train = MNIST(root="data", train=True, download=True, transform=ToTensor())
loader = DataLoader(train, batch_size=128, shuffle=True)

model = nn.Sequential(nn.Flatten(),
                      nn.Linear(28*28, 128), nn.ReLU(),
                      nn.Linear(128, 10))
loss_fn = nn.CrossEntropyLoss()
opt = optim.Adam(model.parameters())

for epoch in range(3):
    for x, y in loader:
        opt.zero_grad()
        loss_fn(model(x), y).backward()
        opt.step()
    print(f"Epoch {epoch}: loss={loss_fn(model(x), y).item():.3f}")
