import RPi.GPIO as GPIO
import time
import getpass

BeepPin = 17  # SAME as your code - active LOW

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' / '
}

DOT = 0.2
DASH = 0.6
INTRA_GAP = 0.2
LETTER_GAP = 0.6
WORD_GAP = 1.4

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BeepPin, GPIO.OUT)
    GPIO.output(BeepPin, GPIO.HIGH)  # HIGH = off

def beep_dot():
    GPIO.output(BeepPin, GPIO.LOW)
    time.sleep(DOT)
    GPIO.output(BeepPin, GPIO.HIGH)
    time.sleep(INTRA_GAP)

def beep_dash():
    GPIO.output(BeepPin, GPIO.LOW)
    time.sleep(DASH)
    GPIO.output(BeepPin, GPIO.HIGH)
    time.sleep(INTRA_GAP)

def send_morse(text):
    text = text.upper()
    for char in text:
        code = MORSE.get(char)
        if not code:
            continue
        if char == ' ':
            print(" / ", end="", flush=True)
            time.sleep(WORD_GAP)
            continue
        # ONLY print dots and dashes, not the letter itself
        print(code + " ", end="", flush=True)
        for symbol in code:
            if symbol == '.':
                beep_dot()
            else:
                beep_dash()
        time.sleep(LETTER_GAP - INTRA_GAP)
    print()  # new line at end

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        while True:
            msg = getpass.getpass("\nEnter secret message (hidden, q to quit): ")
            if msg.lower() == 'q':
                break
            print("Morse: ", end="", flush=True)
            send_morse(msg)
    except KeyboardInterrupt:
        pass
    finally:
        destroy()
