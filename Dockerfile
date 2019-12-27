FROM jjanzic/docker-python3-opencv

RUN pip3 install pipenv


COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

#RUN pip install pipenv


#RUN pip install --no-cache-dir numpy scipy pandas matplotlib
#RUN pipenv install --system --deploy --ignore-pipfile



COPY . /app

# Run server
ENTRYPOINT ["python"]
CMD ["app.py"]