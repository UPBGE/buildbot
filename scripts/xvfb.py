from xvfbwrapper import Xvfb
from print import *

class Display:
	def __init__(self):
		try:
			self.display = Xvfb()
			self.display.start()
		except ErrorReturnCode:
			msgerr("Failed start Xvfb server")
			raise

	def __del__(self):
		try:
			self.display.stop()
		except ErrorReturnCode:
			msgerr("Failed stop Xvfb server")
			raise
