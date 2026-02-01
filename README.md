# mpii-pose-classifier

# Классификация поз людей на изображениях (MPII Human Pose)

Проект создан для классификации изображений людей по видам активности 
(например, dance, swim, run). Модель обучается **с нуля**, без 
предобученных моделей, на датасете MPII Human Pose.


## Структура проекта

src/

<img width="269" height="620" alt="Screenshot 2026-02-01 at 17 27 02" src="https://github.com/user-attachments/assets/fd26f8bc-652d-4a47-8760-247e8f68087a" />



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
