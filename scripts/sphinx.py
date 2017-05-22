from docbuilder import *
from sh import upbge, Command

class SphinxBuilder(DocBuilder):
	def __init__(self):
		DocBuilder.__init__(self, "sphinx")

	def generate(self):
		try:
			cd(blenderSourceDir)
			upbge("--background", "--factory-startup", "-noaudio", "--python", sphinxScript, _out=debugSh, _err=debugSh)
			sphinx = Command("sphinx-build")
			sphinx(sphinxInputDir, sphinxOutputDir, _out=debugSh, _err=debugSh)
		except:
			return False
		return True

if __name__ == "__main__":
	builder = SphinxBuilder()
	builder.update()
	if builder.needGenerate():
		if builder.generate():
			pass #builder.writeCachedHash()
