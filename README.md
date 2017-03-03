# garage-door-opener
Raspberry pi project for opening garage door.

Provisioning raspbian image:

## update all packages & install tools

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip
sudo apt-get install git
```

### web server

```bash
sudo pip install flask
```

### web application

```bash
cd /home/pi  # or wherever you want to host the web app.
git clone https://github.com/BrandonClapp/garage-door-opener
cd garage-door-opener
sudo python server.py # just to ensure that the server starts

# ctrl + d to exit
```

### supervisord

Supervisord will ensure that our web server restarts on boot or server crash.

```bash
sudo apt-get install supervisor
cd /etc/supervisord/
sudo nano supervisord.conf

# At the bottom of the file, add the section for your application.
# i.e. http://stackoverflow.com/a/33591664/1730061

sudo supervisorctl update
sudo supervisorctl status
```

**Example supervisord.conf section**

```
[program:garage-door-opener]                                                                  
command = python server.py                                      
directory = /home/pi/garage-door-opener                            
autostart = true                                                                
autorestart = true
```

## Circuit

**Components needed**
- Cable (20 guage or similar)
- [(Normally Open) Relay](https://www.amazon.com/Tolako-Arduino-Indicator-Channel-Official/dp/B00VRUAHLE/ref=sr_1_4?ie=UTF8&qid=1488514227&sr=8-4&keywords=relay)
  - This project only uses a 1 channel relay for a single garage door, but could easily be modified to use multiple channels for multiple doors.
- Resistor
