import torch
import pandas as pd
from sklearn.metrics import f1_score
from torch.utils.data import DataLoader

from config import DEVICE, TRAIN_CSV, IMAGE_FOLDER, NUM_CLASSES
from dataset import CustomDataset
from transforms import val_transform
from model import PoseNet


def evaluate():
    df = pd.read_csv(TRAIN_CSV)
    dataset = CustomDataset(df, IMAGE_FOLDER, transform=val_transform)
    model = PoseNet(NUM_CLASSES)
    model.load_state_dict(torch.load("model.pth"))
    model.to(DEVICE)
    model.eval()
    y_true, y_pred = [], []

    with torch.no_grad():
        for X, y in DataLoader(dataset, batch_size=32):
            X = X.to(DEVICE)
            preds = model(X)
            y_pred.extend(preds.argmax(1).cpu().tolist())
            y_true.extend(y.tolist())
          
    print("F1-score:", f1_score(y_true, y_pred, average="macro"))
