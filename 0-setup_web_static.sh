#!/usr/bin/env bash
# Sets up the server for deployment of webstatic

#install nginx
if ! command -v nginx &> /dev/null; then
	apt-get -y update
	apt-get -y install nginx
fi

#create required directories
mkdir -p /data/web_static/releases/test /data/web_static/shared

#create html
echo "<html>
      <head>
      </head>
      <body>Holberton School</body>
      </html>
      " | tee /data/web_static/releases/test/index.html > /dev/null
#create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#give ownership to group and user
chown -R ubuntu:ubuntu /data/

nginx_config_content="location /hbnb_static {
	alias /data/web_static/current/;
	index index.html;
}"

sudo sed -i "/server_name _;/a $nginx_config_content" /etc/nginx/sites-available/default

#restart nginx
service nginx restart

exit 0
