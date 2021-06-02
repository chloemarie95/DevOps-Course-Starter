FROM python:3.8 as base 

RUN pip install poetry

WORKDIR /project

FROM base as production

COPY /todo_app /project/todo_app
COPY /templates /project/todo_app
COPY poetry.lock *.toml /project/
COPY .env /project/ 

EXPOSE 5000
RUN poetry install
CMD poetry run flask run --host=0.0.0.0

FROM base as development 