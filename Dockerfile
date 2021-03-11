FROM python:3.8

RUN pip install poetry

WORKDIR /project

COPY /todo_app /project/todo_app
COPY /templates /project/todo_app
COPY poetry.lock *.toml /project/
COPY .env /project/ 

RUN cd /project
RUN poetry install

