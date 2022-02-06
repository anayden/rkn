FROM python:3.9-slim-buster

ADD rkn/ /app/
ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]