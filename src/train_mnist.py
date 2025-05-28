import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

# ------------------------------
# 0. デバイス設定
# ------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ------------------------------
# 1. データセット & Dataloader
# ------------------------------
train_ds = MNIST(root="data", train=True,  download=True, transform=ToTensor())
test_ds  = MNIST(root="data", train=False, download=True, transform=ToTensor())

train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader  = DataLoader(test_ds,  batch_size=512, shuffle=False)

# ------------------------------
# 2. モデル
# ------------------------------
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
).to(device)

print("device =", next(model.parameters()).device)  # ← GPU / CPU を表示

# ------------------------------
# 3. 損失関数 & Optimizer
# ------------------------------
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# ------------------------------
# 4. TensorBoard Writer
# ------------------------------
writer = SummaryWriter(log_dir="runs/mnist")

# ------------------------------
# 5. 学習ループ
# ------------------------------
epochs = 3
for epoch in range(epochs):
    model.train()
    running_loss, correct = 0.0, 0

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        # 順伝播
        logits = model(x)
        loss = criterion(logits, y)

        # 逆伝播 & 更新
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * x.size(0)
        correct += (logits.argmax(1) == y).sum().item()

    # --- 1エポック終了時 ---
    train_loss = running_loss / len(train_ds)
    train_acc  = correct / len(train_ds)

    # 検証
    model.eval()
    val_correct = 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            val_correct += (model(x).argmax(1) == y).sum().item()
    val_acc = val_correct / len(test_ds)

    # TensorBoard へ書き込み
    writer.add_scalar("loss/train", train_loss, epoch)
    writer.add_scalar("acc/train",  train_acc,  epoch)
    writer.add_scalar("acc/val",    val_acc,    epoch)

    print(f"Epoch {epoch} | loss {train_loss:.3f} | train_acc {train_acc*100:.1f}% | val_acc {val_acc*100:.1f}%")

writer.close()
