# mpii-pose-classifier

# Классификация поз людей на изображениях (MPII Human Pose)

Проект создан для классификации изображений людей по видам активности 
(например, dance, swim, run). Модель обучается **с нуля**, без 
предобученных моделей, на датасете MPII Human Pose.

## Структура проекта

src/
config.py — пути, гиперпараметры
dataset.py — датасет PyTorch
transforms.py — аугментации и преобразования
model.py — архитектура нейросети
train.py — обучение модели
evaluate.py — оценка качества
utils.py — графики и вспомогательные функции

## Как запустить обучение
python3 src/train.py

## Оценка модели
python3 src/evaluate.py

Метрика качества: **macro F1-score**.

## ⚙️ Технологии
- Python, PyTorch
- torchvision, PIL
- matplotlib
- sklearn
