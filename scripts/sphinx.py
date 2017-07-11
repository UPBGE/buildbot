from docbuilder import *
from sh import upbge, Command
import shutil
import sys

class SphinxBuilder(DocBuilder):
	def __init__(self):
		DocBuilder.__init__(self, "sphinx")

	def generate(self, rebuild):
		try:
			cd(blenderSourceDir)
			if rebuild:
				shutil.rmtree(sphinxInputDir, sphinxOutputDir)
			upbge("--background", "--factory-startup", "-noaudio", "--python", sphinxScript, _out=debugSh, _err=debugSh)
			sphinx = Command("sphinx-build")
			sphinx(sphinxInputDir, sphinxOutputDir, _out=debugSh, _err=debugSh)
		except:
			return False
		return True

if __name__ == "__main__":
	builder = SphinxBuilder()
	builder.update()
	rebuild = ("--rebuild" in sys.argv)

	if builder.needGenerate():
		if builder.generate(rebuild):
			pass #builder.writeCachedHash()
