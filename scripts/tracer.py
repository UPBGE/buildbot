from common import *
from tester import Tester
from print import *
from sh import mkdir, Command
from glob import glob
from PIL import Image, ImageChops
import math, operator
from functools import reduce

class FileTracer:
	def __init__(self, branch, hash, testFile, traceDirectory, imageDirectory):
		self.branch = branch
		self.testFile = testFile
		self.traceDirectory = traceDirectory
		self.imageDirectory = imageDirectory

	def trace(self):
		try:
			mkdir("-p", self.traceDirectory)
			cmd = Command(self.blenderplayer)
			cmd.run("-p", traceMainScript, self.testFile, "-", self.imageDirectory, _out=debugSh)
		except ErrorReturnCode:
			msgerr("Failed trace branch {} blenderplayer".format(self.branch))
			return False
		else:
			msgstat("Sucess trace branch {} blenderplayer".format(self.branch))

	def getImages(self):
		images = glob(self.imageDirectory + "*.png")
		images.sort()
		return images

class BranchTracer(Tester):
	def __init__(self, branch, hash):
		Tester.__init__(self, branch, traceMainScript, ())
		self.hash = hash
		self.imageDirectory = imageDir + self.branch + "_" + self.hash + "/"

	def runFile(self, blendFile):
		imageDir = self.imageDirectory + blendFile.split("/")[-1].replace(".blend", "") + "/"
		try:
			cmd = Command(self.blenderplayer)
			upbgeargs = ("-p", self.pythonMainScript, blendFile, "-", imageDir)
			cmd.run(upbgeargs, _out=debugSh)
		except ErrorReturnCode:
			return False
		return True


def compareImages(images1, images2):
	if len(images1) == 0 or len(images2) == 0:
		msgerr("Invalid image lists to compare")
		return

	minsize = min(len(images1), len(images2))

	images1 = images1[0:minsize]
	images2 = images2[0:minsize]

	diffs = []
	for image1, image2 in zip(images1, images2):
		#msgcmd("Compare image {} and {}".format(image1, image2))

		try:
			im1 = Image.open(image1)
			im2 = Image.open(image2)
		except:
			msgerr("Failed open image files {} and {}".format(image1, image2))

		diff = ImageChops.difference(im1, im2)
		h = diff.histogram()
		val = math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(im1.size[0]) * im1.size[1]))
		diffs.append(val)

	return diffs

if __name__ == "__main__":
	branches = (BranchTracer("master", "0000"), BranchTracer("ge_blender_glsl", "0000"))

	for tracer in branches:
		tracer.run()

	"""images = []
	for branch in branches:
		filetrace = branch.tracer(testFiles + "Render/Material/Color/meshColor.blend")
		if not "--no-trace" in sys.argv:
			filetrace.trace()
		images.append(filetrace.getImages())

	diffs = compareImages(images[0], images[1])

	for i, diff in enumerate(diffs):
		if diff < 0.1:
			msgstat("Images at frame {} are same, difference of {}".format(i, diff))
		elif diff < 1:
			msgwarn("Images at frame {} are fuzzy, difference of {}".format(i, diff))
		else:
			msgerr("Images at frame {} does not math difference of {}".format(i, diff))"""
		
