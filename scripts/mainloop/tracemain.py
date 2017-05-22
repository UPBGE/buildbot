import bge
import time

for i in range(10):
	t = time.time()
	bge.logic.NextFrame()
	f = time.time()
	if (f - t) < 0.1:
		time.sleep(0.1 - (f - t))
	print("Frame:", i)
