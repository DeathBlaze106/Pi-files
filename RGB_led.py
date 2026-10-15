import RPi.GPIO as GPIO
import time

# SunFounder wiring
R_PIN = 17
G_PIN = 18
B_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([R_PIN, G_PIN, B_PIN], GPIO.OUT)

# Start HIGH = OFF for common-anode
GPIO.output(R_PIN, GPIO.HIGH)
GPIO.output(G_PIN, GPIO.HIGH)
GPIO.output(B_PIN, GPIO.HIGH)

pwm_r = GPIO.PWM(R_PIN, 2000)
pwm_g = GPIO.PWM(G_PIN, 2000)
pwm_b = GPIO.PWM(B_PIN, 2000)

# Start at 100 = OFF for common-anode
pwm_r.start(100)
pwm_g.start(100)
pwm_b.start(100)

def setColor(r, g, b):
    # r,g,b = 0-255
    # Invert: 0 -> 100% off? No, we want 255 = ON = 0% duty
    r_duty = 100 - (r / 255 * 100)
    g_duty = 100 - (g / 255 * 100)
    b_duty = 100 - (b / 255 * 100)
    
    pwm_r.ChangeDutyCycle(r_duty)
    pwm_g.ChangeDutyCycle(g_duty)
    pwm_b.ChangeDutyCycle(b_duty)

try:
    print("RED")
    setColor(255, 0, 0)
    time.sleep(1)
    
    print("GREEN")
    setColor(0, 255, 0)
    time.sleep(1)
    
    print("BLUE")
    setColor(0, 0, 255)
    time.sleep(1)
    
    print("YELLOW = Red + Green")
    setColor(255, 255, 0)
    time.sleep(1)

    print("CYAN")
    setColor(0, 255, 255)
    time.sleep(1)

    print("MAGENTA")
    setColor(255, 0, 255)
    time.sleep(1)

    print("WHITE")
    setColor(255, 255, 255)
    time.sleep(2)

except KeyboardInterrupt:
    pass
finally:
    pwm_r.stop()
    pwm_g.stop()
    pwm_b.stop()
    GPIO.cleanup()
