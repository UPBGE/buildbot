from xvfb import *
from sh import Command, apitrace
from common import *
from print import *
import sys

display = Display()

if "--branch" in sys.argv:
	branch = sys.argv[sys.argv.index("--branch") + 1]
else:
	branch = "master"

blenderplayer = prefixBuildBranchDir + branch + "/bin/blenderplayer"

args = ("-p", traceMainScript, testFiles + "Render/Wire/WireMaterial.blend", "-", homeDir)

if "simple" in sys.argv:
	cmd = Command(blenderplayer)
	cmd.run(*args, _out=debugSh)
elif "trace" in sys.argv:
	tracefile = traceDir + branch
	apitrace("trace", "-o", tracefile, blenderplayer, *args, _out=debugSh)
