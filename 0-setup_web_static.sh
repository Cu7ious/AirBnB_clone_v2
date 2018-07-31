#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data
sudo chown -R ubuntu:ubuntu /data

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

read -r -d '' HTML <<- EOM
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOM

echo -e "$HTML" > /data/web_static/releases/test/index.html

ln -sfn /data/web_static/releases/test/ /data/web_static/current

line="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "38i $line" /etc/nginx/sites-available/default

sudo service nginx restart
