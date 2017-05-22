import sys
import os
from common import *
from branch import *
from irc import *
from print import *
from sh import git, cd
from collections import OrderedDict

branchesValid = []
branchesCompiled = []
branchesFailed = []

def processBranch(branch, release=False, compress=True):
	global branchesValid
	global branchesCompiled
	global branchesFailed

	branchesValid.append(branch)
	if not "--no-pull" in sys.argv:
		branch.update()
	if branch.needCompile() or "--force" in sys.argv:
		branchesCompiled.append(branch)
		if not "--no-build" in sys.argv:
			if not branch.build():
				#client.sendError("Failed build branch " + branch.name)
				branchesFailed.append(branch)
				return False

		if not "--test" in sys.argv:
			if branch.findName(release):
				if not "--no-compress" in sys.argv and compress:
					if branch.compress():
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
		#print(mask.read())
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

	branch = Branch(branch, tag=tag, builder=ReleaseBaseBuilder())
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

	branch = Branch(branch, tag=tag, builder=BranchDebugBuilder())
	processBranch(branch, compress=False)
