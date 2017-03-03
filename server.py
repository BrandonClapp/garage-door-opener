from flask import Flask, render_template, send_from_directory
import time
#import RPi.GPIO as GPIO

app = Flask(__name__, static_url_path='')

pin = 12
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin, GPIO.OUT)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/scripts/<path:path>')
def send_scripts(path):
    return send_from_directory('scripts', path)

@app.route("/trigger/", methods=['POST'])
def trigger():
    #GPIO.output(pin, True)
    print('Triggered')
    time.sleep(0.5)
    #GPIO.output(pin, False)
    return ('', 204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
