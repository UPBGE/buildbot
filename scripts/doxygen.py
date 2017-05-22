from docbuilder import *
from sh import doxygen

class DoxygenBuilder(DocBuilder):
	def __init__(self):
		DocBuilder.__init__(self, "doxygen")

	def generate(self):
		cd(doxygenDir)
		try:
			doxygen(doxygenConfigFile, _out=debugSh)
		except:
			return False
		return True

if __name__ == "__main__":
	builder = DoxygenBuilder()
	builder.update()
	if builder.needGenerate():
		if builder.generate():
			pass#builder.writeCachedHash()
