#!/bin/bash

mkdir -p /home/box/web
cp /home/box/web/Module1_9/Step11/hello.py /home/box/web/hello.py
cp /home/box/web/Module1_9/Step11/gunicorn.conf /home/box/web/etc/gunicorn.conf

sudo ln -sf /home/box/web/Module2_1/Step11/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart
