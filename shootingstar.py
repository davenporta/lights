import time
import board
import neopixel
import math

pixel_pin = board.D18
num_pixels=1009

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write = False, brightness=0.8, pixel_order=ORDER)

def wheel(pos):

	if pos < 0 or pos > 1:
		r = g = b = 0
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

array = [(0, 0, 0)]*num_pixels

def array_advance(array):
	array2 =[0]*len(array)
	for j in range(num_pixels-2):
		array2[j+1] = array[j]
	array2[0] = array[-1]
	return(array2)


pixels.fill((255, 255, 255))
pixels.show()
time.sleep(0.5)


tail = 50
tailarr = [10**(x/25) for x in range(-50, 0)]
numcol = 3

#colarr = [x/(numcol-1) for x in range(numcol-1)]
#colarr.append(1.0)
#print(colarr)

colarr = [0, 1/3, 2/3]

arr1=[1]*num_pixels
for n in range(num_pixels):
	arr1[n]=1*colarr[math.floor(n/tail)%numcol]
	array[n] = wheel(arr1[n])

for n in range(num_pixels):
	subarr = array[n]
	subarr = [int(x*tailarr[n%tail]) for x in array[n]]
	array[n] = subarr

print(tailarr)

while True:
	for i in range(num_pixels):
		pixels[i] = array[i]
	#for j in range(5):
	array = array_advance(array)

	pixels.show()
