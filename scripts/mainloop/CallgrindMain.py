import bge
import time
import subprocess

for i in range(10):
	if bge.logic.KX_INPUT_JUST_ACTIVATED in bge.logic.keyboard.inputs[bge.events.ESCKEY].queue:
		exit = True
		break

	t = time.time()
	bge.logic.NextFrame()
	f = time.time()
	if (f - t) < 0.1:
		time.sleep(0.1 - (f - t))
	print("Frame:", i)

	if i == 1:
		subprocess.call(["callgrind_control", "-i", "on"])
	if i == 9:
		subprocess.call(["callgrind_control", "-i", "off"])
