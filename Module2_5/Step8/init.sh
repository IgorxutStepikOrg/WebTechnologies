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

mkdir -p /home/box/web/ask/templates

cp /home/box/web/Module2_5/Step8/ask/ask/settings.py /home/box/web/ask/ask/settings.py
cp /home/box/web/Module2_5/Step8/ask/ask/urls.py /home/box/web/ask/ask/urls.py
cp /home/box/web/Module2_5/Step8/ask/qa/models.py /home/box/web/ask/qa/models.py
cp /home/box/web/Module2_5/Step8/ask/qa/urls.py /home/box/web/ask/qa/urls.py
cp /home/box/web/Module2_5/Step8/ask/qa/views.py /home/box/web/ask/qa/views.py
cp /home/box/web/Module2_5/Step8/ask/templates/main.html /home/box/web/ask/templates/main.html
cp /home/box/web/Module2_5/Step8/ask/templates/list.html /home/box/web/ask/templates/list.html
cp /home/box/web/Module2_5/Step8/ask/templates/question.html /home/box/web/ask/templates/question.html

cp /home/box/web/Module2_5/Step8/nginx.conf /home/box/web/etc/nginx.conf
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

cp /home/box/web/Module2_5/Step8/gunicorn.conf /home/box/web/etc/gunicorn.conf
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart

cd /home/box/web/ask/
echo >> ./ask/settings.py
python manage.py syncdb
