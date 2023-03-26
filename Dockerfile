FROM python:3.9-slim-buster
LABEL Maintainer="OsmanKandemir"
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python", "indicator.py"]


#docker build -t indicator .
#docker run indicator --domains target-web.com --json
