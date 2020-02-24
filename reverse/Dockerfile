FROM python:3.7
LABEL maintainer="Suresh Rayapalli"
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install requests
EXPOSE 5000
ENTRYPOINT ["python", "/app/reverse.py"]
