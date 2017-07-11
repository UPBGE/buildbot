from common import *
from print import *
from sh import Command, ErrorReturnCode, valgrind
import os
from threading import Thread, RLock

class RunFileThread(Thread):
	def __init__(self, tester, file):
		Thread.__init__(self)
		self.tester = tester
		self.file = file

	def run(self):
		if not self.tester.runFile(self.file):
			self.tester.addFailure(self.file)

class Tester:
	def __init__(self, branch, pythonMainScript, args):
		self.branch = branch
		self.blenderplayer = prefixBuildDebugDir + self.branch + "/bin/blenderplayer"
		self.pythonMainScript = pythonMainScript
		self.args = args
		self.failures = []
		self.lock = RLock()

	def addFailure(self, file):
		with self.lock:
			self.failures.append(file)

	def run(self):
		files = [(s + os.sep + f) for s, d, fs in os.walk(testFiles) for f in fs if (s + os.sep + f).endswith(".blend")]

		tasks = []
		for i, blendFile in enumerate(files):
			msgcmd("[{:03d}/{:03d}] Run branch {} with file {}".format(i, len(files), self.branch, blendFile))
			task = RunFileThread(self, blendFile)
			task.start()
			tasks.append(task)

			if len(tasks) > 3:
				tasks[0].join()
				tasks.pop(0)

		if len(self.failures) > 0:
			msgerr("Branch %s as failures" % self.branch)
			for fail in self.failures:
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
