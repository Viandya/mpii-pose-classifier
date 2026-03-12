## Развертывание в Kubernetes

1. Сборка образа:
   ```bash
   docker build -t pose-classifier:latest . 
2. Загрузка в registry:
   ```bash
   docker push your-registry/pose-classifier:latest
3. Применение манифестов:
   ```bash
   kubectl apply -f k8s/
4. Проверка:
   ```bash
   kubectl get pods
   kubectl port-forward svc/pose-classifier-service 8080:80

# Деплой MPII Pose Classifier

### Предварительные требования
- Python 3.9+
- pip
- Git

### Установка
```bash
# Клонирование репозитория
git clone https://github.com/yourusername/mpii-pose-classifier.git
cd mpii-pose-classifier

### Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

### Установка зависимостей
```bash
pip install -r requirements.txt

### Установка dev-зависимостей
```bash
pip install pytest pytest-cov black flake8
