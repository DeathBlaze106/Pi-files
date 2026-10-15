import RPi.GPIO as GPIO
import time

R=17
G=18
B=27

GPIO.setmode(GPIO.BCM)
GPIO.setup([R,G,B], GPIO.OUT)

# Try COMMON-CATHODE logic first (HIGH = ON)
print("Testing as Common-Cathode: HIGH=ON")
for pin, name in [(R,"RED"), (G,"GREEN"), (B,"BLUE")]:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    print(f" {name} should be ON now - is it?")
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)

print("\nTesting as Common-Anode: LOW=ON")
for pin, name in [(R,"RED"), (G,"GREEN"), (B,"BLUE")]:
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    print(f" {name} should be ON now - is it?")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)

GPIO.cleanup()
