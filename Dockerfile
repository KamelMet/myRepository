FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app/"

RUN apt update -y && apt install -y python3-pip && pip3 install -r requirements.txt

CMD ["python", "basicmlapp/main.py"]
