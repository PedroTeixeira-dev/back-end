FROM 3.12.2-alpine3.18 AS base

ARG APP_USER=ipc

ARG APP_HOME=/app

RUN adduser --disabled-password --gecos '' ${APP_USER}
RUN adduser ${APP_USER} sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV PYTHONUNBUFFERED 1

RUN apt update \
  && apt install -y libpq-dev gcc

RUN pip install --upgrade pip pipenv

WORKDIR ${APP_HOME}

COPY Pipfile ${APP_HOME}

COPY Pipfile.lock ${APP_HOME}

RUN pipenv install --system --deploy

COPY . ${APP_HOME}

EXPOSE 80

RUN chmod ugo+rwx -R /app

CMD /bin/sh -c "flask db upgrade -d back-end/migrations; \
  gunicorn --config gunicorn_config.py wsgi:application"