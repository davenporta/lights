import time
import board
import neopixel

pixel_pin = board.D18
num_pixels=960

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write = False, brightness=0.5, pixel_order=ORDER)

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


#pixels.fill((255, 255, 255))
pixels.show()
time.sleep(1)
phase = 0.0
inc = 1/(255*5)
while True:
	pixels.fill(wheel(phase))
	#pixels.fill((phase, 0, 0))
	pixels.show()
	print(phase)
	phase += inc
	if phase > 1:
		phase -= 1
	#time.sleep(.5)
