FROM python:3.11

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements /usr/src/app/requirements
RUN pip install -r requirements/production.txt

COPY . /usr/src/app

RUN apt-get update \
    && apt-get install -y netcat-traditional \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/bin/nc.traditional /usr/bin/nc

COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
EXPOSE 8000
