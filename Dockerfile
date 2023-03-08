FROM python:3.9
LABEL Maintainer="OsmanKandemir"
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python", "indicator/indicator_docker.py"]


#docker build -t indicator .
#docker run indicator --domain google.com
