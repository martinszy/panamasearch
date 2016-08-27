FROM python:2.7-onbuild

RUN python /usr/src/app/manage.py migrate

CMD ["python", "/usr/src/app/manage.py","runserver","0.0.0.0:5000"]

EXPOSE 5000