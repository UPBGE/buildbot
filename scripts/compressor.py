from print import *
from common import *
from sh import tar, md5sum, ErrorReturnCode

class Compressor:
	def compress(self, buildDir, archive):
		msgcmd("Compress archive", archive)
		try:
			tar("-Jvcf", archive, "-C", buildDir + "/bin", ".", _env={"XZ_OPT" : "-9e"}, _out=debugSh)
			md5 = str(md5sum(archive)).split(" ")[0]
			msgstat("Archive md5 ", md5)
			with open(archive + ".md5", "w") as md5file:
				md5file.write(md5)
		except:
			msgerr("Failed compress archive", archive)
			return False

		msgstat("Finished compress archive", archive)
		return True
