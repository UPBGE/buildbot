from common import *
from print import *
from sh import Command, ErrorReturnCode, valgrind
import os

class Tester:
	def __init__(self, branch, pythonMainScript, args):
		self.branch = branch
		self.blenderplayer = prefixBuildDebugDir + self.branch + "/bin/blenderplayer"
		self.pythonMainScript = pythonMainScript
		self.args = args
		print(self.blenderplayer)

	def run(self):
		failures = []
		for subdir, dirs, files in os.walk(testFiles):
			for file in files:
				blendFile = subdir + os.sep + file
				if blendFile.endswith(".blend"):
					msgcmd("Run branch {} with file {}".format(self.branch, blendFile))
					if not self.runFile(blendFile):
						failures.append(blendFile)

		if len(failures) > 0:
			msgerr("Branch %s as failures" % self.branch)
			for fail in failures:
				msgerr("Failed run file: %s" % fail)

	def runFile(self, blendFile):
		try:
			cmd = Command(self.blenderplayer)
			upbgeargs = ("-p", self.pythonMainScript, blendFile)
			if len(self.args) > 0:
				upbgeargs += ("-", self.args)
			cmd.run(upbgeargs, _out=debugSh)
		except ErrorReturnCode:
			return False
		return True

class Valgrind(Tester):
	def runFile(self, blendFile):
		try:
			logFile = valgrindLogDir + blendFile.replace(testFiles, "").replace("/", "_").replace(".blend", ".log")
			valargs = ("--log-file={}".format(logFile), "--leak-check=full", "--suppressions={}".format(valgrindSuppressionsFile))
			upbgeargs = (self.blenderplayer, "-p", self.pythonMainScript, blendFile)
			if len(self.args) > 0:
				upbgeargs += ("-", self.args)
			valgrind(valargs + upbgeargs, _out=debugSh)
		except ErrorReturnCode:
			return False
		return True
