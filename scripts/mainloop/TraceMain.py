import BasicMain
import bge
import sys

class TraceMain(BasicMain.BasicMain):
	def __init__(self, directory):
		BasicMain.BasicMain.__init__(self)
		self.directory = directory

	def endFrame(self, i):
		if i == 0:
			# First frame wasn't yet rendered at this stage.
			return
		filename = self.directory + str(i).rjust(3, "0") + ".png"
		bge.render.makeScreenshot(filename)

if __name__ == "__main__":
	BasicMain.launch(TraceMain(sys.argv[-1]))
