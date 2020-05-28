FROM python:3.7-slim-buster
RUN apt update -y 
RUN apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app/"
CMD ["python", "correction/application/main.py"]