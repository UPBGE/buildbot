from tester import *
from sh import git, cd
import sys

cd(blenderSourceDir)
git.remote("prune", "origin")
git.pull("--rebase")

if "--branch" in sys.argv:
	branch = sys.argv[sys.argv.index("--branch") + 1]
else:
	branch = "master"

args = []
if "basic" in sys.argv:
	script = "BasicMain"
if "error" in sys.argv:
	script = "PythonErrorMain"
	args = [pythonTestLogDir]

scriptFile = pythonMainScript + script + ".py"

if "valgrind" in sys.argv:
	tester = Valgrind(branch, scriptFile, args)
else:
	tester = Tester(branch, scriptFile, args)

tester.run()

