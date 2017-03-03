# garage-door-opener
Raspberry pi project for opening garage door.

Provisioning raspbian image:

## update all packages & install python-pip

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install pip
```

### web server

```bash
sudo pip install flask
```

### web application

```bash
cd ~/application/hosting/path # wherever we want to host the web app.
git clone https://github.com/BrandonClapp/garage-door-opener
cd garage-door-opener
sudo python server.py # just to ensure that the server starts

# ctrl + d to exit
```

### supervisord

Supervisord will ensure that our web server restarts on boot or server crash.

```bash
sudo apt-get install supervisord
cd /etc/supervisord/
sudo nano supervisord.conf

# add the section for your application. i.e. http://stackoverflow.com/a/33591664/1730061

sudo supervisorctl update
sudo supervisorctl status
```
