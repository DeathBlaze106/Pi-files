import RPi.GPIO as GPIO
import time

LedPin = 18  # BCM 18 = hardware PWM, perfect for breathing

def setup():
    global p
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
    p = GPIO.PWM(LedPin, 1000)  # 1000Hz frequency
    p.start(0)                  # 0% brightness to start

def loop():
    while True:
        for dc in range(0, 101, 4):      # 0 to 100%
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -4):    # 100 to 0%
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)

def destroy():
    global p
    p.stop()          # STOP PWM first - this fixes your __del__ error
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    finally:
        # safety net if destroy() wasn't called
        try:
            p.stop()
        except:
            pass
        GPIO.cleanup()
