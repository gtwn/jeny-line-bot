FROM python


WORKDIR /app

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5050

ENTRYPOINT [ "python3"]
CMD ["app.py"]
# FROM ubuntu

# RUN apt-get update -y 
# RUN apt-get install -y python3-pip python3-dev

# # We copy just the requirements.txt first to leverage Docker cache

# WORKDIR /app

# COPY requirements.txt ./requirements.txt

# RUN pip3 install -r requirements.txt

# COPY . .

# # ENTRYPOINT [ "python3" ]

# CMD [ "python3","app.py" ]