from tester import *
from tracer import *
from xvfb import *
from sh import git, cd
import sys

display = Display()

cd(blenderSourceDir)
git.remote("prune", "origin")
git.pull("--rebase")

if "--branch" in sys.argv:
	branch = sys.argv[sys.argv.index("--branch") + 1]
else:
	branch = "master"

args = []
script = ""
if "basic" in sys.argv:
	script = "BasicMain"
elif "error" in sys.argv:
	script = "PythonErrorMain"
	args = [pythonTestLogDir]

scriptFile = pythonMainScript + script + ".py"

if "valgrind" in sys.argv:
	tester = Valgrind(branch, scriptFile, args)
elif "tracer" in sys.argv:
	tester = BranchTracer(branch, "0000")
else:
	tester = Tester(branch, scriptFile, args)

tester.run()

