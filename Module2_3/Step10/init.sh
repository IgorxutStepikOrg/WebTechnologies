#!/bin/bash

mkdir -p {/home/box/web/public/{img,css,js},/home/box/web/{uploads,etc}}

cd /home/box/web
django-admin startproject ask

cd /home/box/web/ask/
python manage.py startapp qa

cp /home/box/web/Module2_3/Step10/ask/ask/urls.py /home/box/web/ask/ask/urls.py
cp /home/box/web/Module2_3/Step10/ask/qa/urls.py /home/box/web/ask/qa/urls.py
cp /home/box/web/Module2_3/Step10/ask/qa/views.py /home/box/web/ask/qa/views.py
cp /home/box/web/Module2_3/Step10/ask/qa/models.py /home/box/web/ask/qa/models.py

cat /home/box/web/ask/ask/settings.py | sed "s/'django.contrib.staticfiles',/'django.contrib.staticfiles',\n    'qa',/" > temp_txt && sudo mv temp_txt /home/box/web/ask/ask/settings.py
cat /home/box/web/ask/ask/settings.py | sed "s/'ENGINE': 'django.db.backends.sqlite3',/'ENGINE': 'django.db.backends.mysql',/" > temp_txt && sudo mv temp_txt /home/box/web/ask/ask/settings.py
cat /home/box/web/ask/ask/settings.py | sed "s/'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),/'NAME': 'db_ask',\n        'USER': 'user_ask',\n        'PASSWORD': 'pass_ask',\n        'HOST': 'localhost',\n        'PORT': '',/" > temp_txt && sudo mv temp_txt /home/box/web/ask/ask/settings.py

sudo ln -sf /home/box/web/Module2_3/Step10/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/Module2_3/Step10/gunicorn.conf /etc/gunicorn.d/default
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE db_ask DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
mysql -u root -e "CREATE USER 'user_ask' IDENTIFIED BY 'pass_ask';"
mysql -u root -e "GRANT ALL PRIVILEGES ON db_ask.* TO 'user_ask';"
mysql -u root -e "FLUSH PRIVILEGES;"

cd /home/box/web/ask/
sudo python manage.py syncdb

#end
