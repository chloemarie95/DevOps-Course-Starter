FROM python:3.8 as base 

ENTRYPOINT /bin/bash 

RUN pip install poetry
WORKDIR /project

COPY poetry.lock *.toml /project/
COPY docker-entrypoint.sh ./
COPY /todo_app /project/todo_app
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

FROM base as test
COPY .env.test /project/
COPY /tests/ /project/tests/
COPY /e2e_test /project/e2e_test
COPY poetry.lock pyproject.toml /project/
COPY /todo_app /project/todo_app
RUN cd /project/
RUN poetry install
ENTRYPOINT ["poetry", "run", "pytest", "tests"]

FROM base as e2e_test
COPY .env.test /project/
COPY /tests/ /project/tests/
COPY /e2e_test /project/e2e_test
COPY poetry.lock pyproject.toml /project/
COPY /todo_app /project/todo_app
RUN cd /project/
RUN poetry install
# Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chromestable_current_amd64.deb -o chrome.deb &&\
apt-get install ./chrome.deb -y &&\
rm ./chrome.deb

# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
echo "Installing chromium webdriver version ${LATEST}" &&\
curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
apt-get install unzip -y &&\
unzip ./chromedriver_linux64.zip

ENTRYPOINT ["poetry", "run", "pytest", "e2e_test"]