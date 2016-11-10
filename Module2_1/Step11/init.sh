#!/bin/bash

sudo apt-get -y update
sudo apt-get -y upgrade

sudo pip3 install django
sudo pip3 install gunicorn

cat /usr/sbin/gunicorn-debian | sed 's/python/python3/g' > test && sudo mv test /usr/sbin/gunicorn-debian
cat /usr/bin/gunicorn | sed 's/17.5/19.6.0/g' > test && sudo mv test /usr/bin/gunicorn
cat /usr/bin/gunicorn | sed 's/python/python3/g' > test && sudo mv test /usr/bin/gunicorn
cat /usr/bin/gunicorn | sed 's/17.5/19.6.0/g' > test && sudo mv test /usr/bin/gunicorn_django
cat /usr/bin/gunicorn | sed 's/python/python3/g' > test && sudo mv test /usr/bin/gunicorn_django
cat /usr/bin/gunicorn | sed 's/17.5/19.6.0/g' > test && sudo mv test /usr/bin/gunicorn_paster
cat /usr/bin/gunicorn | sed 's/python/python3/g' > test && sudo mv test /usr/bin/gunicorn_paster

mkdir -p /home/box/web

cd /home/box/web
django-admin startproject ask

cd /home/box/web/ask
python manage.py startapp qa

cp /home/box/web/Module2_1/Step11/ask/qa/views.py /home/box/web/ask/qa/views.py
cp /home/box/web/Module2_1/Step11/ask/qa/urls.py /home/box/web/ask/qa/urls.py
cp /home/box/web/Module2_1/Step11/ask/ask/urls.py /home/box/web/ask/ask/urls.py

sudo ln -sf /home/box/web/Module2_1/Step11/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart
