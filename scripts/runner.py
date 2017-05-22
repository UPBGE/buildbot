from common import *
from print import *
from sh import Command, ErrorReturnCode

class Runner:
	def getVersion(self, branch, blenderplayer):
		try:
			cmd = Command(blenderplayer)
			cmd.run(printVersionFile, printVersionBlendFile, _out=debugSh)
		except ErrorReturnCode:
			msgerr("Failed run branch {} blenderplayer".format(branch))
			return False
		else:
			msgstat("Sucess run branch {} blenderplayer".format(branch))

		with open(printVersionFile, "r") as file:
			lines = file.readlines()
			blenderVersion = lines[0][0:-1]
			upbgeVersion = lines[1][0:-1]

			msgstat("blender version: {}, UPBGE version: {}".format(blenderVersion, upbgeVersion))

			return (blenderVersion, upbgeVersion)
