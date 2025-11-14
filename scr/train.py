import torch
import pandas as pd
from torch.utils.data import DataLoader
from torch import optim, nn

from config import DEVICE, TRAIN_CSV, IMAGE_FOLDER, NUM_CLASSES, BATCH_SIZE, EPOCHS, LR
from dataset import CustomDataset
from transforms import train_transform
from model import PoseNet


def train():
    train_df = pd.read_csv(TRAIN_CSV)
    dataset = CustomDataset(train_df, IMAGE_FOLDER, transform=train_transform)
    model = PoseNet(NUM_CLASSES).to(DEVICE)
    loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LR)
    for epoch in range(EPOCHS):
        model.train()
        epoch_loss = 0
        for X, y in loader:
            X, y = X.to(DEVICE), y.to(DEVICE)
            optimizer.zero_grad()
            preds = model(X)
            loss = criterion(preds, y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f"Epoch {epoch+1}/{EPOCHS}, loss = {epoch_loss / len(loader):.4f}")
    torch.save(model.state_dict(), "model.pth")


if __name__ == "__main__":
    train()
