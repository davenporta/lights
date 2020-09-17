import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 1009

ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, pixel_order=ORDER)

rate = 0.1

code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        '.': '.-.-.-', '!': '-.-.--', '?': '..--..',

        ' ': '/'}

timing = {'.': [1, 0], '-': [1, 1, 1, 0], ' ': [0, 0], '/': [0, 0]}


def to_morse(s):
	# encode message to morse
	try:
		phrase = ' '.join(code[i.upper()] for i in s)
		print("Sending: " + phrase)
	except:
		print("Invalid character!")
		return
	
	# morse code to binary timing sequence
	timecode = []
	for c in list(phrase):
		timecode += timing[c]
	
	# signal message start
	pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(1)
	pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(1)
	pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(0.5)

	# display message
	for bit in timecode:
		pixels.fill((255*bit, 0, 0))
		pixels.show()
		time.sleep(rate)	
	
	# wait after message end
	pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(1)
    
while True:
	pixels.fill((0, 0, 0))
	pixels.show()
	to_morse(input("Message to Send: "))
