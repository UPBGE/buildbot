import sys
import bge
import BasicMain

scene = bge.logic.getCurrentScene()

def validCamera():
	return (scene.active_camera.name != "__default__cam__")

def scanKeyboardSensors():
	for scene in bge.logic.getSceneList():
		for obj in scene.objects + scene.objectsInactive:
			for sensor in obj.sensors:
				if type(sensor) in (bge.types.SCA_KeyboardSensor, bge.types.SCA_MouseSensor, bge.types.SCA_JoystickSensor):
					return True
	if hasattr(bge.app, "upbge_version"):
		if len(bge.logic.getInactiveSceneNames()) != 0:
			return True
	return False

class UserTestMain(BasicMain.BasicMain):
	def __init__(self, durationNoSensors, durationSensors):
		BasicMain.BasicMain.__init__(self, frame=-1)
		self.durationNoSensors = durationNoSensors
		self.durationSensors = durationSensors

	def init(self):
		if not validCamera():
			print("Invalid default camera, exiting.")
			return False
		return BasicMain.BasicMain.init(self)

	def run(self):
		duration = self.durationSensors if scanKeyboardSensors() else self.durationNoSensors
		startTime = bge.logic.getFrameTime()
		print(startTime)
		while bge.logic.getFrameTime() < (startTime + duration):
			bge.logic.NextFrame()

if __name__ == "__main__":
	BasicMain.launch(UserTestMain(5, 10))
