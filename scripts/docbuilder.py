from common import *
from updater import *

class DocBuilder:
	def __init__(self, docname):
		self.name = "master"
		self.docname = docname
		self.updater = Updater()
		self.hashFile = branchHashDir + self.docname + ".txt"

	def update(self):
		self.updater.pull(self.name, "", docDir)
		self.commitHash = self.updater.getHash(docDir)

	def needGenerate(self):
		return self.updater.needCompile(self.name, self.hashFile, self.commitHash)

	def writeCachedHash(self):
		self.updater.writeCachedHash(self.hashFile, self.commitHash)
