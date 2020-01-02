FROM jjanzic/docker-python3-opencv

RUN pip3 install pipenv


COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# Run server
ENTRYPOINT ["python"]
CMD ["app.py"]