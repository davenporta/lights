import time
import board
import neopixel

pixel_pin = board.D18
num_pixels=960

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write = False, brightness=0.1, pixel_order=ORDER)

def wheel(pos):

	if pos < 0 or pos > 255:
		r = g = b = 0
	elif pos < 85:
		r = int(pos*3)
		g = int(255-pos*3)
		b = 0
	elif pos < 170:
		pos -= 85
		r = int(255-pos*3)
		g = 0
		b = int(pos*3)
	else:
		pos -= 170
		r = 0
		g = int(pos*3)
		b = int(255-pos*3)
	return (r, g, b)

array = [x%240 for x in range(num_pixels)]

def array_advance(array):
	first = array[0]
	for j in range(num_pixels-1):
		array[j] = array[j+1]
	array[-1] = first
	return(array)


pixels.fill((255, 0, 0))
pixels.show()
time.sleep(1)

pixels.fill((0, 255, 0))
pixels.show()
time.sleep(1)

pixels.fill((0, 0, 255))
pixels.show()
time.sleep(1)

n = 0
while True:
	for i in range(num_pixels):
		pixels[i] = wheel(array[i])
	array = array_advance(array)
	pixels.show()
