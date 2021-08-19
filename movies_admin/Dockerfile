FROM python:3.9.5

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/base.txt requirements/dev.txt requirements/production.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r dev.txt

COPY . .

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
