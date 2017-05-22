import bge
import time
import sys

exit = False
frametime = 0.004
time = bge.logic.getRealTime()

frames = 0

while frames < 10:
	ctime = bge.logic.getRealTime()
	timestep = ctime - time
	if (timestep) > frametime:
		bge.logic.NextFrame()
		frames += 1
		print("Frame:", frames, time)
		time = ctime

if "--restart" in sys.argv:
	print("restart")
	bge.logic.restartGame()
	bge.logic.NextFrame()

