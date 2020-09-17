import time
import board
import neopixel

pixel_pin = board.D18
num_pixels=1009

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=.4, pixel_order=ORDER)

pixels.fill((255, 208, 170))
pixels.show()

time.sleep(1)

