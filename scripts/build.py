import sys
import os
from common import *
from branch import *
from irc import *
from print import *
from xvfb import *
from sh import git, cd
from collections import OrderedDict

display = Display()

branchesValid = []
branchesCompiled = []
branchesFailed = []

def failedBranch(branch):
	global branchesFailed
	branchesFailed.append(branch)

def compiledBranch(branch):
	global branchesCompiled
	branchesCompiled.append(branch)

def validBranch(branch):
	global branchesValid
	branchesValid.append(branch)

def processBranch(branch, release=False, compress=True):
	validBranch(branch)
	if not "--no-pull" in sys.argv:
		branch.update()

	if not branch.needCompile() and not "--force" in sys.argv:
		return True

	compiledBranch(branch)

	if not "--no-build" in sys.argv:
		rebuild = ("--rebuild" in sys.argv)
		if not branch.build(rebuild):
			failedBranch(branch)
			return False

	if "--only-build" in sys.argv:
		return True

	if not branch.check():
		failedBranch(branch)
		return False

	if not branch.findName(release):
		failedBranch(branch)
		return False

	if "--no-compress" in sys.argv or not compress:
		return True

	if not branch.compress():
		failedBranch(branch)
		return False

	# All operation succeed for the current compiled version.
	branch.writeCachedHash()

	return True

if "branch" in sys.argv:
	#client = IrcClient()
	cd(blenderSourceDir)
	git.remote("prune", "origin")
	git.pull("--rebase")
	git.remote("prune", "origin")

	if "--branch" in sys.argv:
		branchNames = [sys.argv[sys.argv.index("--branch") + 1]]
	else:
		branchNames = str(git.branch("--all", "--color=never")).split(" ")
		branchNames = [name[15:-1] for name in branchNames if name.startswith("remotes/origin") and name != "remotes/origin/HEAD"]

	with open(branchMaskFile, "a+") as mask:
		mask.seek(0)
		maskBranch = [line[:-1] for line in mask.readlines()]
		for branchName in branchNames:
			if not os.path.exists(prefixSourceDir + "blender_" + branchName) and not branchName in maskBranch:
				while True:
					answer = input("Do you want mask branch " + branchName + "? (y/n): ")
					if answer == "y":
						mask.write(branchName + "\n")
						break;
					elif answer == "n":
						break;

		# update mask list
		mask.seek(0)
		maskBranch = [line[:-1] for line in mask.readlines()]
		for branchName in branchNames:
			if branchName in maskBranch:
				msgwarn("Masked branch", branchName)
				continue

			branch = Branch(branchName)
			processBranch(branch)

	with open(logDir + "build_summary.txt", "w") as logFile:
		msglog("Build summary:", log=logFile)
		categories = OrderedDict([
			("Branches: ", branchesValid),
			("Branches compiled: ", branchesCompiled),
			("Branches failed: ", branchesFailed)
				])

		for category, branches in categories.items():
			msglog(category, log=logFile)
			for branch in branches:
				msglog("\t - ", branch.name, log=logFile)

if "release" in sys.argv:
	cd(blenderSourceDir)
	if not "--no-pull" in sys.argv:
		git.remote("prune", "origin")
		git.pull("--rebase")
		git.remote("prune", "origin")

	branch = "master"
	tag = ""
	if "--branch" in sys.argv:
		branch = sys.argv[sys.argv.index("--branch") + 1]

	if "--tag" in sys.argv:
		tag = sys.argv[sys.argv.index("--tag") + 1]

	branch = Branch(branch, _hashDir=releaseHashDir, tag=tag, builder=ReleaseBaseBuilder())
	processBranch(branch, release=True)

if "debug" in sys.argv:
	cd(blenderSourceDir)
	git.remote("prune", "origin")
	git.pull("--rebase")
	git.remote("prune", "origin")

	branch = "master"
	tag = ""
	if "--branch" in sys.argv:
		branch = sys.argv[sys.argv.index("--branch") + 1]

	if "--tag" in sys.argv:
		tag = sys.argv[sys.argv.index("--tag") + 1]

	branch = Branch(branch, _hashDir=debugHashDir, tag=tag, builder=BranchDebugBuilder())
	processBranch(branch, compress=False)
