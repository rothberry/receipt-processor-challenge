FROM python:3.8.13

RUN pip install pipenv

ENV PROJECT_DIR .

COPY . /${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy


CMD ["flask", "run"]