from builder import *
from sender import *
from runner import *
from updater import *
from compressor import *
from datetime import datetime

class Branch:
	def __init__(self, name, tag="", builder=BranchBaseBuilder(), builderDebug=BranchDebugBuilder()):
		self.name = name
		self.tag = tag
		self.sourceDir = prefixSourceDir + "blender_" + name
		self.buildDir = builder.prefixBuildDir + name
		self.buildDebugDir = builderDebug.prefixBuildDir + name
		self.blenderplayer = self.buildDir + "/bin/blenderplayer"
		self.releaseDir = releaseDir
		self.hashFile = branchHashDir + self.name + ".txt"
		self.commitHash = "test"

		self.logFile = open(buildLogDir + name + ".txt", "w")
		setLogFile(self.logFile)

		self.builder = builder
		self.builderDebug = builderDebug
		self.runner = Runner()
		self.updater = Updater()
		self.compressor = Compressor()
		self.sender = Sender()

	def __del__(self):
		self.logFile.close()

	def update(self):
		self.updater.pull(self.name, self.tag, self.sourceDir)
		self.commitHash = self.updater.getHash(self.sourceDir)

	def needCompile(self):
		return self.updater.needCompile(self.name, self.hashFile, self.commitHash)

	def writeCachedHash(self):
		self.updater.writeCachedHash(self.hashFile, self.commitHash)

	def build(self):
		if not self.builder.build(self.name, self.sourceDir, self.buildDir):
			return False;

		self.builder.strip(self.name, self.buildDir)

		#if not self.builderDebug.build(self.name, self.sourceDir, self.buildDebugDir):
			#return False

		return True

	def findName(self, release):
		versions = self.runner.getVersion(self.name, self.blenderplayer)
		if versions == False:
			return False

		if release:
			self.releaseName = "UPBGEv{}b{}Linux64".format(versions[1], versions[0])
			self.releaseArchive = linuxReleaseDir + self.releaseName + ".tar.xz"
		else:
			currentDate = datetime.now()
			dateStr = "{}{:02d}{}".format(currentDate.day, currentDate.month, currentDate.year)
			self.releaseName = "UPBGE_{}_v{}b{}d{}h{}Linux64".format(self.name, versions[1], versions[0], dateStr, self.commitHash)
			self.releaseArchive = linuxBranchDir + self.releaseName + ".tar.xz"

		return True

	def compress(self):
		return self.compressor.compress(self.buildDir, self.releaseArchive)

	def send(self):
		pass#return self.sender.send(self.releaseArchive, self.serverReleaseArchive)

if __name__ == "__main__":
	branch = Branch("ge_glsl_inverse")
	branch.update()
	if branch.needCompile():
		if branch.build():
			if branch.findName():
				branch.compress()
				branch.send()
				branch.writeCachedHash()
