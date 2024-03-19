FROM python:alpine

WORKDIR /modules/score

RUN pip install flask

COPY . .

CMD ["flask", "--app", "main_score", "run", "--host", "0.0.0.0"]

# run using "docker run -d -p 5000:5000 wogapi:latest"