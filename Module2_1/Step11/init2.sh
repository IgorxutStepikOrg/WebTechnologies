#!/bin/bash

sudo apt-get update
sudo pip3 install virtualenv

sudo ln -sf /home/box/web/Module2_1/Step11/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

virtualenv -p python3 env
source env/bin/activate

sudo pip3 install django
sudo pip3 install gunicorn

mkdir -p {/home/box/web/public/{img,css,js},/home/box/web/{uploads,etc}}

cd /home/box/web
django-admin startproject ask

cd /home/box/web/ask
python3 manage.py startapp qa

cp /home/box/web/Module2_1/Step11/ask/qa/views.py /home/box/web/ask/qa/views.py
cp /home/box/web/Module2_1/Step11/ask/ask/urls.py /home/box/web/ask/ask/urls.py

cat /home/box/web/ask/ask/settings.py | sed "s/'django.contrib.staticfiles',/'django.contrib.staticfiles',\n    'qa',\n/" > temp_txt && sudo mv temp_txt /home/box/web/ask/ask/settings.py

sudo ln -sf /home/box/web/Module2_1/Step11/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart

#end
