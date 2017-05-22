from sh import rsync
from common import *
from print import *
import server
import sys

serverHomeDir = "git@" + server.ip + ":/home/git/"
serverDownloadDir = serverHomeDir + "download/"

doxygenClientDir = homeDir + "doxygen/"
doxygenServerDir = serverHomeDir + "doxygen/"

sphinxClientDir = homeDir + "pythonapi/"
sphinxServerDir = serverHomeDir + "pythonapi/"

serverLogDir = serverDownloadDir + "buildbot/logs"

branchServerDir = serverDownloadDir + "buildbot/branch/"

releaseServerDir = serverDownloadDir + "release/linux64/"

win32Dir = homeDir + "download/release/windows32/"
win64Dir = homeDir + "download/release/windows32/"

win32ServerDir = serverDownloadDir + "release/windows32/"
win64ServerDir = serverDownloadDir + "release/windows64/"

options = ["-e", "ssh", "-avz", "-AX", "--info=progress2"]

def sync(source, target, delete=False):
	try:
		if delete:
			opt = options + ["--delete-after"]
		else:
			opt = options
		msgstat("Syncing {} with {}".format(source, target))
		rsync(opt, source, target, _out=debugSh, _err=debugSh)
	except:
		msgerr("Failed syncing {} with {}".format(source, target))
	else:
		msgstat("Success syncing {} with {}".format(source, target))

logFile = open(logDir + "sync.txt", "w")
setLogFile(logFile)

if "doxygen" in sys.argv:
	sync(doxygenClientDir, doxygenServerDir)

if "pythonapi" in sys.argv:
	sync(sphinxClientDir, sphinxServerDir)

if "branch" in sys.argv:
	sync(linuxBranchDir, branchServerDir, True)

if "release" in sys.argv:
	sync(linuxReleaseDir, releaseServerDir)

if "windows" in sys.argv:
	sync(win32ServerDir, win32Dir)
	sync(win64ServerDir, win64Dir)

if "logs" in sys.argv:
	sync(logDir, serverLogDir)

logFile.close()
