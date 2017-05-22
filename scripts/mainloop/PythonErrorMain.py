import sys
import traceback
import BasicMain

class PythonErrorMain(BasicMain.BasicMain):
	def __init__(self, logFileDir):
		BasicMain.BasicMain.__init__(self)
		filename = sys.argv[-3].replace("/home/tristan/files/", "").replace("/", "_").replace(".blend", ".log")
		print(logFileDir + filename)
		self.log = open(logFileDir + filename, "w")
		self.log.write(("*" * 30) + " " + filename + " " + ("*" * 30) + "\n")

	def __del__(self):
		self.log.close()

	def exceptHook(self, exctype, value, tb):
		print("Detect error")
		self.log.write("=" * 100 + "\n")
		traceback.print_exception(exctype, value, tb, file=self.log)

	def init(self):
		sys.excepthook = self.exceptHook
		return BasicMain.BasicMain.init(self)

if __name__ == "__main__":
	BasicMain.launch(PythonErrorMain(sys.argv[-1]))
