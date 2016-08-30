FROM python:2.7-onbuild

RUN python /usr/src/app/manage.py migrate

RUN pip install supervisor

COPY supervisord.conf /etc/

RUN apt-get update && apt-get install -y cron

RUN crontab crontab.txt

CMD ["supervisord", "-n"]

EXPOSE 5000