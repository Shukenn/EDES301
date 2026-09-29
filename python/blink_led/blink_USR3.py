import Adafruit_BBIO.GPIO as GPIO
import time

LED = "USR3"
HALF_PERIOD = 0.1   # 5 Hz = 0.2s per cycle = 0.1s on, 0.1s off

GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(HALF_PERIOD)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(HALF_PERIOD)
except KeyboardInterrupt:
    GPIO.cleanup()