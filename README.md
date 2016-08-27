# panamasearch
MediaParty 2016

#Instalación
`git clone https://github.com/martinszy/panamasearch.git`
`cd panamasearch`
`mkvirtualenv panamasearch`
`pip install -r requirements.txt`
`./manage.py migrate`
`./manage.py runserver`

Para ejecutar el proceso offline de los csv:
(usando el python dentro del virtualenv)
`python manage.py processcsv`
