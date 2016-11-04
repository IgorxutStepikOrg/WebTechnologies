#!/bin/bash

mkdir -p /home/box/web/etc
cp /home/box/web/Module1_9/Step11/hello.py /home/box/web/hello.py
cp /home/box/web/Module1_9/Step11/gunicorn.conf.py /home/box/web/etc/gunicorn.conf.py

sudo ln -sf /home/box/web/Module1_9/Step11/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart
