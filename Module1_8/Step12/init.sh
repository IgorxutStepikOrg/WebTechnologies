mkdir -p {~/web/public/{img,css,js},~/web/{uploads,etc}}
cp ~/web/Module1_8/Step12/nginx.conf ~/web/etc/nginx.conf

sudo ln -sf ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
