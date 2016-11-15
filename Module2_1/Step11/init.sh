#!/bin/bash

mkdir -p {/home/box/web/public/{img,css,js},/home/box/web/{uploads,etc}}

cd /home/box/web
django-admin startproject ask

cd /home/box/web/ask
python manage.py startapp qa

cp /home/box/web/Module2_3/Step10/ask/ask/settings.py /home/box/web/ask/ask/settings.py
cp /home/box/web/Module2_1/Step11/ask/ask/urls.py /home/box/web/ask/ask/urls.py
cp /home/box/web/Module2_1/Step11/ask/qa/urls.py /home/box/web/ask/qa/urls.py
cp /home/box/web/Module2_1/Step11/ask/qa/views.py /home/box/web/ask/qa/views.py

sudo ln -sf /home/box/web/Module2_1/Step11/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/Module2_1/Step11/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart

cd /home/box/web/ask/
echo >> ./ask/settings.py
