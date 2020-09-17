import time
import board
import neopixel

pixel_pin = board.D18
num_pixels=1010

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


def array_advance(array):
	first = array[0]
	for j in range(num_pixels-1):
		array[j] = array[j+1]
	array[-1] = first
	return(array)

array = [(float(x)*2/num_pixels)%1 for x in range(num_pixels)]

pixels.fill((255, 255, 255))
pixels.show()
time.sleep(1)

while True:
	for j in range(5):
		array = array_advance(array)
	temparray=array
	for k in range(int(num_pixels/10)):
		temparray[k*10] = 2
	for i in range(num_pixels):
		pixels[i] = wheel(temparray[i])
	pixels.show()
