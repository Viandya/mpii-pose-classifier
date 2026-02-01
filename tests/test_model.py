import pytest
import torch
from src.model import PoseClassifier

def test_model_output_shape():
    model = PoseClassifier(num_classes=10)
    dummy_input = torch.randn(1, 3, 256, 256)
    output = model(dummy_input)
    assert output.shape == (1, 10)
