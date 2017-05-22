from common import *
from server import *
from print import *
from sh import md5sum

class Sender:
	def __init__(self):
		pass

	def send(self, releaseArchive, serverReleaseArchive):
		md5 = str(md5sum(releaseArchive)).split(" ")[0]
		with open(releaseArchive + ".md5", "w") as md5file:
			md5file.write(md5)

		if sendFile(releaseArchive + ".md5", serverReleaseArchive + ".md5") and sendFile(releaseArchive, serverReleaseArchive):
			return True
		return False

