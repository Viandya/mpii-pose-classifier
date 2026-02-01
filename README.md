# mpii-pose-classifier

# Классификация поз людей на изображениях (MPII Human Pose)

Проект создан для классификации изображений людей по видам активности 
(например, dance, swim, run). Модель обучается **с нуля**, без 
предобученных моделей, на датасете MPII Human Pose.


## Структура проекта

<img width="263" height="547" alt="Screenshot 2026-02-01 at 18 03 46" src="https://github.com/user-attachments/assets/4ec4e197-83aa-4563-9c5c-2950dcb5a829" />




## Как запустить обучение
python3 src/train.py

## Оценка модели
python3 src/evaluate.py

Метрика качества: **macro F1-score**.

## Технологии
- Python, PyTorch
- torchvision, PIL
- matplotlib
- sklearn

### Docker
```bash
# Сборка образа
docker build -t mpii-pose-classifier:latest .

# Запуск контейнера
docker run -p 8000:8000 mpii-pose-classifier:latest
