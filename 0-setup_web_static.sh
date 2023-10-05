#!/usr/bin/env bash
# script thatsets up your server for deployment

#install nginx
sudo apt-get update
sudo apt-get install -y nginx

#create folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#create a html file for test
echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" >> /data/web_static/releases/test/index.html

#create and recreate a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownwership to ubuntu user
sudo chown -R ubuntu:ubuntu /data/

#update nginx and config to server
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

#restart nginx
sudo service nginx restart
