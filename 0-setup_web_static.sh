#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

#    Install Nginx if it not already installed
#    Create the folder /data/ if it doesn’t already exist
#    Create the folder /data/web_static/ if it doesn’t already exist
#    Create the folder /data/web_static/releases/ if it doesn’t exist
#    Create the folder /data/web_static/shared/ if it doesn’t exist
#    Create the folder /data/web_static/releases/test/ if it doesn’t exist
#    Create an HTML file /data/web_static/releases/test/index.html
#        with a simple content
#    Create a symbolic link /data/web_static/current linked to
#        the /data/web_static/releases/test/ folder.
#        If the symbolic link already exists, it should be deleted
#        and recreated every time the script is ran.
#    Give ownership of the /data/ folder to the ubuntu user AND group
#        (assuming this user and group exists). This should be recursive
#        Everything inside should be created/owned by this user/group.
#    Update the Nginx configuration to serve the content of
#        /data/web_static/current/ to hbnb_static
#        ex: https://mydomainname.tech/hbnb_static
sudo apt-get update && sudo apt-get install nginx

sudo mkdir /data
sudo chown -R ubuntu:ubuntu /data

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

read -r -d '' HTML <<- EOM
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>NginX Test</title>
  </head>
  <body>
    <h1>NginX Test</h1>
    <p>If you can read this, your NginX is runnining
	and it has been properly configured.</p>
  </body>
</html>
EOM

echo -e "$HTML" > /data/web_static/releases/test/index.html

ln -sfn /data/web_static/releases/test/ /data/web_static/current

line="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "38i $line" /etc/nginx/sites-available/default

sudo service nginx restart
