FROM python:3.5
ENV PYTHONUNBUFFERED 1

ADD ./requirements/local.txt /requirements/local.txt

ADD ./requirements/base.txt /requirements/base.txt

ADD ./requirements/production.txt /requirements/production.txt

ADD ./entrypoint.sh /entrypoint.sh

ADD . /bootcamp

RUN pip install -r ./requirements/local.txt

RUN groupadd -r django && useradd -r -g django django

RUN chown -R django /bootcamp && chmod +x entrypoint.sh && chown django entrypoint.sh

WORKDIR /bootcamp

ENTRYPOINT ["/entrypoint.sh"]
