from common import *
from print import *
from os import path
from sh import git, cd, cp

class Updater:
	def pull(self, branch, tag, sourceDir):
		if not path.exists(sourceDir):
			msgwarn("Source directory {} non-existing".format(sourceDir))
			cp("-R", blenderSourceDir, sourceDir)
		cd(sourceDir)

		msgcmd("Update branch {}".format(branch))

		#git.rebase("--abort")
		git.clean("-fd", _out=debugSh)
		git.checkout(".", _out=debugSh)

		try:
			git.checkout("-t", "origin/" + branch, _out=debugSh)
		except:
			pass

		git.checkout(branch)

		git.pull("origin", branch, "--rebase", _out=debugSh)
		git.remote("prune", "origin")

		git.pull("--rebase", _out=debugSh)
		if tag is not "":
			git.checkout(tag, _out=debugSh)

		git.submodule.foreach("--recursive", "git", "checkout", "master", _out=debugSh)
		git.submodule.foreach("git", "reset", "HEAD", "--hard", _out=debugSh)
		git.submodule.update("--init", "--recursive", _out=debugSh)
		git.submodule.foreach("--recursive", "git", "pull", "--rebase", "origin", "master", _out=debugSh)

	def getHash(self, sourceDir):
		cd(sourceDir)
		hash = git("rev-parse", "HEAD")
		return str(hash)[:7]

	def needCompile(self, branch, hashFile, newHash):
		oldHash = ""
		if path.exists(hashFile):
			with open(hashFile, "r") as file:
				oldHash = file.readlines()[0][:7]
				if oldHash == newHash:
					msgstat("Building branch {} skipped".format(branch))
					return False
		else:
			msgcmd("No branch {} hash file".format(branch))

		msgstat("Building branch {} needed, old hash: {}, new hash: {}".format(branch, oldHash, newHash))
		return True

	def writeCachedHash(self, hashFile, newHash):
		with open(hashFile, "w") as file:
			file.write(newHash)
