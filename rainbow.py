import time
import board
import neopixel

pixel_pin = board.D18
num_pixels=960

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, pixel_order=ORDER)

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


def rainbow_cycle(wait):
	for j in range(255):
		for i in range(num_pixels):
			pixel_index=i
			pixels[i] = wheel(j)
		pixels.show()
		time.sleep(wait)


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
	pixels[n%960] = wheel(n%255)
	n += 1
	pixels.show()
