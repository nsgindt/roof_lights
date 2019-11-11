#!/usr/bin/env python

"""A demo client for Open Pixel Control
http://github.com/zestyping/openpixelcontrol

Sends red, green, and blue to the first 3 LEDs.

To run:
First start the gl simulator using, for example, the included "wall" layout

    make
    bin/gl_server layouts/wall.json

Then run this script in another shell to send colors to the simulator

    python_clients/example.py

"""

import time
import random
import opc

ADDRESS = '192.168.1.51:7890'

# Create a client object1
client = opc.Client(ADDRESS)


rainbow_array = [0 for i in range(0,512)]
[rainbow_array.append(i-512) for i in range(512,768)]
[rainbow_array.append(255) for i in range(768,1280)]
[rainbow_array.append(1535-i) for i in range(1280,1536)]




num_lights=92

# Test if it can connect
if client.can_connect():
    print ('connected') 
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print ('not connected')

# Send pixels forever
#for i in range(100):
increment =0
string = [(0,0,0) for i in range(num_lights)]
my_wait=.5
while True:
    #my_pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    #random.shuffle(my_pixels)
    # if client.put_pixels(my_pixels, channel=0):
    #     print ('sent')
    # else:
    #     print ('not sent')
    # time.sleep(0.3)
	for i in range(num_lights):
		rVal=(i*10 + increment) % 1536 
		gVal=(i*10 + increment + 512) % 1536 
		bVal=(i*10 + increment + 1024) % 1536
		string[i] = (rainbow_array[rVal],rainbow_array[bVal],rainbow_array[gVal])
	client.put_pixels(string)
	increment = increment + 10
	time.sleep(.1)
	# client.put_pixels([(255,0,0) for i in range(num_lights)])
	# time.sleep(my_wait)
	# client.put_pixels([(255,255,0) for i in range(num_lights)])
	# time.sleep(my_wait)
	# client.put_pixels([(0,255,0) for i in range(num_lights)])
	# time.sleep(my_wait)
	# client.put_pixels([(0,255,255) for i in range(num_lights)])
	# time.sleep(my_wait)
	# client.put_pixels([(0,0,255) for i in range(num_lights)])
	# time.sleep(my_wait)
	# client.put_pixels([(255,0,255) for i in range(num_lights)])
	# time.sleep(my_wait)