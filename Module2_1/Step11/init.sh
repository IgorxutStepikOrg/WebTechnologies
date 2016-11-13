#!/bin/bash

#sudo apt-get -y update

#sudo apt-get -y remove gunicorn

#sudo pip3 install django
#sudo pip3 install gunicorn

sudo pip install --upgrade django
sudo pip install --upgrade gunicorn

mkdir -p {/home/box/web/public/{img,css,js},/home/box/web/{uploads,etc}}

django-admin startproject /home/box/web/ask
python manage.py startapp /home/box/web/ask/qa

cp /home/box/web/Module2_1/Step11/ask/qa/views.py /home/box/web/ask/qa/views.py
cp /home/box/web/Module2_1/Step11/ask/ask/urls.py /home/box/web/ask/ask/urls.py

cat /home/box/web/ask/ask/settings.py | sed "s/'django.contrib.staticfiles',/'django.contrib.staticfiles',\n    'qa',\n/" > temp_txt && sudo mv temp_txt /home/box/web/ask/ask/settings.py

sudo ln -sf /home/box/web/Module2_1/Step11/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/Module2_1/Step11/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart

#end
