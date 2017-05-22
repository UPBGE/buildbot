import pickle
import time
import sys
import bge

print(sys.argv)

frames = 30

profiles = []

time.sleep(.5)
for i in range(frames):
	bge.logic.NextFrame()
	if i > frames * 0.1:
		info = bge.logic.getProfileInfo()
		profiles.append((bge.logic.getRealTime(), dict(info)))
	time.sleep(0.01)

filename = "/home/tristan/TestFiles/Profile/Logs/" + sys.argv[-1].split("/")[-1].replace(".blend", ".profile") + sys.argv[-2]
with open(filename, "wb") as file:
	print("write to", filename)
	pickle.dump(profiles, file)
