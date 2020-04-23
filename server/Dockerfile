FROM python:3.7-slim
WORKDIR /app
COPY . /app
RUN pip install -qr requirements.txt
RUN pip install -e .
EXPOSE 8080