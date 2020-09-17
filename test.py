import time
import board
import neopixel

pixel_pin = board.D18
num_pixels=300

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, pixel_order=ORDER)

pixels.fill((255, 255, 255))
pixels.show()

time.sleep(1)

