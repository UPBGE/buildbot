import bge
import time
import sys

sys.path.append("/home/tristan/TestFiles/PythonMain/")

import gccheck

start = time.time()
duration = 5.0

while time.time() < start + duration:
	if bge.logic.KX_INPUT_JUST_ACTIVATED in bge.logic.keyboard.inputs[bge.events.ESCKEY].queue:
		break

	bge.logic.NextFrame()

gccheck.gcCheck()
