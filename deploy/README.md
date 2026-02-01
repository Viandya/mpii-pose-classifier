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
