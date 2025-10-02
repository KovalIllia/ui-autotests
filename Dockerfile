FROM python:3.9-slim

WORKDIR /app

COPY . /app/

ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y chromium chromium-driver


RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest allure-python-commons pytest-html pytest-xdist webdriver-manager

RUN mkdir -p /output/test_result

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "pytest", "-s", "--alluredir=/output/test_result"]