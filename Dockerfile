FROM python:3.8 as base 

ENTRYPOINT /bin/bash 

RUN pip install poetry
WORKDIR /project

COPY poetry.lock *.toml /project/
COPY docker-entrypoint.sh ./
COPY /todo_app /project/todo_app
COPY /templates /project/todo_app
COPY .env /project/ 

EXPOSE 5000

FROM base as prod
RUN cd /project/
RUN poetry install
CMD ["./docker-entrypoint.sh"]

FROM base as dev
COPY /tests/ /project/tests/
COPY docker-flask-entrypoint.sh ./docker-entrypoint.sh
RUN cd /project/
RUN poetry install
CMD ["./docker-entrypoint.sh"]