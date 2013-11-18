rasppi
======

Raspberry Pi I2C thermometer


Necessary configuration
=======================
Install mysql, create database named 'monitor' with user 'root' and password 'toor'.
apt-get install libapache2-mod-wsgi 

settings.py
===========
	change TEMPLATE_DIRS to correct absolute path.

apache config
=============

Alias /static/ /home/q/rasppi/rpi/static/

<Directory /home/q/rasppi/rpi/static>
Order deny,allow
Require all granted
</Directory>

WSGIScriptAlias / /home/q/rasppi/rpi/rpi/wsgi.py
WSGIPythonPath /home/q/rasppi/rpi/

<Directory /home/q/rasppi/rpi/rpi>
<Files wsgi.py>
Order deny,allow
Require all granted
</Files>
</Directory>
              
Static Files
============
chmod 644 static/*