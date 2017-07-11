from common import *
from print import *
from ldd import ldd

class Checker:
	def __init__(self):
		with open(libsListFile, "r") as file:
			self.libs = [s.replace("\n", "") for s in file.readlines()]

	def checkLibs(self, binary):
		libs = ldd((binary,))
		
		if len(libs) == 0:
			msgerr("Invalid library list")
			return False

		ret = True
		for lib in libs:
			if lib not in self.libs:
				msgerr("Forbidden library dependency {}".format(lib))
				ret = False
		return ret

	def check(self, branch, binaries):
		ret = True
		for binary in binaries:
			if self.checkLibs(binary):
				msgstat("Binary {} succeed library check".format(binary))
			else:
				msgerr("Binary {} failed library check".format(binary))
				ret = False
		return ret
