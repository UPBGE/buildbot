import sys

logFile = None

def msgstat(*argv):
	print("\033[1;32m*\033[1;m", *argv)

def msgcmd(*argv):
	print(">>>", *argv)

def msgerr(*argv):
	print("\033[1;31m*\033[1;m", *argv)

def msgwarn(*argv):
	print("\033[1;33m*\033[1;m", *argv)

def msglog(*argv, log):
	print(*argv)
	if logFile is not None:
		print(*argv, file=log)

if "--debug" in sys.argv:
	def debugSh(*argv):
		if logFile is not None:
			print(*argv, end="", file=logFile)
			logFile.flush()
		print(*argv, end="")
else:
	debugSh = None

def setLogFile(file):
	global logFile
	logFile = file

if __name__ == "__main__":
	msgstat("Status")
	msgcmd("Command")
	msgerr("Error")
	msgwarn("Warning")
