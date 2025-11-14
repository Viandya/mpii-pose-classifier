import torch

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available()
    else "cpu"
)

DATA_PATH = "data/"
IMAGE_FOLDER = "data/img_train/"
TEST_FOLDER = "data/img_test/"
TRAIN_CSV = "data/train_answers.csv"
ACTIVITY_CATEGORIES = "data/activity_categories.csv"

NUM_CLASSES = 20
BATCH_SIZE = 32
EPOCHS = 20
LR = 0.0001
