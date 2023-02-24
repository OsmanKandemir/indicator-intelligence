LABEL Maintainer="OsmanKandemir"
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirement.txt
CMD ["python", "indicator/indicator_docker.py"]


#docker build -t indicator .
#docker run indicator --domain google.com
