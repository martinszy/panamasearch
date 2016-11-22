PAPATH="/var/www/leaksearch"
echo "Stopping container $(< $PAPATH/.containerid) from $PAPATH/.containerid"
docker stop "$(< $PAPATH/.containerid)"
rm "$PAPATH/.containerid"
docker pull cubetto/panamasearch:latest
docker run -v "$PAPATH/db.sqlite3:/usr/src/app/db.sqlite3" cubetto/panamasearch:latest python /usr/src/app/manage.py migrate 
docker run -d -v "$PAPATH/uploadcsv/static:/usr/src/app/Uploadcsv/static"  -v "$PAPATH/data:/usr/src/app/data"  --cidfile "$PAPATH/.containerid" -p 5000:5000 cubetto/panamasearch:latest
