from common import *
from print import *
from os import path
from sh import cd, Command, pwd, cmake, make, ErrorReturnCode, mkdir, strip, rm

class BaseBuilder:
	def build(self, branch, sourceDir, buildDir, rebuild):
		msgcmd("Building branch {}".format(branch))
		try:
			if not path.exists(buildDir):
				mkdir("-p", buildDir)
			elif path.exists(buildDir + "/bin") and rebuild:
				rm("-rf", buildDir + "/bin")

			cd(buildDir)
			cmake("-C", self.configFile, sourceDir, _out=debugSh, _err=debugSh)
			cd(sourceDir)
			make("BUILD_DIR=" + buildDir, "NPROCS=4", _out=debugSh, _err=debugSh)
		except ErrorReturnCode as e:
			msgerr("Failed build branch {}".format(branch))
			return False
		else:
			msgstat("Sucess build branch {}".format(branch))
			return True

	def strip(self, branch, buildDir):
		fileNames = ["blender", "blenderplayer", "makesdna", "makesrna", "datatoc", "datatoc_icon"]
		msgcmd("Strip branch {} binaries".format(branch))
		for name in fileNames:
			strip("-sX", buildDir + "/bin/" + name)

class DebugBuilder:
	def build(self, branch, sourceDir, buildDir, rebuild):
		msgcmd("Building branch debug {}".format(branch))
		try:
			if not path.exists(buildDir):
				mkdir("-p", buildDir)
			elif path.exists(buildDir + "/bin") and rebuild:
				rm("-rf", buildDir + "/bin")

			cd(buildDir)
			cmake("-C", self.configFile, sourceDir, _out=debugSh, _err=debugSh)
			cd(sourceDir)
			make("debug", "BUILD_DIR=" + buildDir, "NPROCS=4", _out=debugSh, _err=debugSh)
		except ErrorReturnCode as e:
			msgerr("Failed build branch debug {}".format(branch))
			return False
		else:
			msgstat("Sucess build branch debug {}".format(branch))
			return True

	def strip(self, branch, buildDir):
		pass

class ReleaseBaseBuilder(BaseBuilder):
	def __init__(self):
		self.configFile = releaseConfigFile
		self.prefixBuildDir = prefixBuildReleaseDir

class BranchBaseBuilder(BaseBuilder):
	def __init__(self):
		self.configFile = liteConfigFile
		self.prefixBuildDir = prefixBuildBranchDir

class BranchDebugBuilder(DebugBuilder):
	def __init__(self):
		self.configFile = debugConfigFile
		self.prefixBuildDir = prefixBuildBranchDebugDir

if __name__ == "__main__":
	builder = ReleaseBuilder()
	builder.build()
