from flask import Flask, render_template
import time
#import RPi.GPIO as GPIO

app = Flask(__name__)

pin = 12
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin, GPIO.OUT)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/trigger/", methods=['POST'])
def trigger():
    #GPIO.output(pin, True)
    time.sleep(0.5)
    #GPIO.output(pin, False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=False)
