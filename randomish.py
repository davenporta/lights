import time
import board
import neopixel
import numpy

pixel_pin = board.D18
num_pixels=960

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write = False, brightness=0.1, pixel_order=ORDER)

def wheel(pos):

	if pos < 0 or pos > 1:
		r = g = b = 255
	elif pos < 1/3:
		r = int(pos*255*3)
		g = int(255-pos*255*3)
		b = 0
	elif pos < 2/3:
		pos -= 1/3
		r = int(255-pos*255*3)
		g = 0
		b = int(pos*255*3)
	else:
		pos -= 2/3
		r = 0
		g = int(pos*255*3)
		b = int(255-pos*255*3)
	return (r, g, b)

array = [(float(x)*2/num_pixels)%1 for x in range(num_pixels)]

def array_advance(array):
	first = array[0]
	for j in range(num_pixels-1):
		array[j] = array[j+1]
	array[-1] = first
	return(array)


pixels.fill((255, 255, 255))
pixels.show()
time.sleep(1)

while True:
	
	pixels[numpy.random.randint(0, num_pixels-1)] = wheel(numpy.random.uniform())
	pixels.show()
