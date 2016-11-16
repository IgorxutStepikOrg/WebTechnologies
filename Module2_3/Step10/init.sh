#!/bin/bash

mkdir -p {/home/box/web/public/{img,css,js},/home/box/web/{uploads,etc}}

sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE db_ask DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
mysql -u root -e "CREATE USER 'user_ask' IDENTIFIED BY 'pass_ask';"
mysql -u root -e "GRANT ALL PRIVILEGES ON db_ask.* TO 'user_ask';"
mysql -u root -e "FLUSH PRIVILEGES;"

cd /home/box/web
django-admin startproject ask

cd /home/box/web/ask/
python manage.py startapp qa

cp -f /home/box/web/Module2_3/Step10/ask/ask/settings.py /home/box/web/ask/ask/settings.py
cp -f /home/box/web/Module2_3/Step10/ask/ask/urls.py /home/box/web/ask/ask/urls.py
cp -f /home/box/web/Module2_3/Step10/ask/qa/models.py /home/box/web/ask/qa/models.py
cp -f /home/box/web/Module2_3/Step10/ask/qa/urls.py /home/box/web/ask/qa/urls.py
cp -f /home/box/web/Module2_3/Step10/ask/qa/views.py /home/box/web/ask/qa/views.py

sudo ln -sf /home/box/web/Module2_3/Step10/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/Module2_3/Step10/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart

cd /home/box/web/ask/
# echo >> ./ask/settings.py
python manage.py syncdb
