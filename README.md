docker
# збірка образу
docker build -t pytest_runner .

# запуск контейнера з мапінгом результатів
docker run -v $(pwd)/output/test_result:/output/test_result pytest_runner
