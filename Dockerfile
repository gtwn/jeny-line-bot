# FROM python:3.8


# WORKDIR /app

# COPY . /app


# RUN pip3 --no-cache-dir install -r requirements.txt

# EXPOSE 8080

# ENTRYPOINT [ "python3"]
# CMD ["app.py"]
FROM ubuntu

RUN apt-get update -y 
RUN apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]