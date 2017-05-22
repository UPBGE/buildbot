from common import *
from print import *
from sh import mkdir, apitrace
from glob import glob
from PIL import Image, ImageChops
import math, operator
from functools import reduce

class FileTrace:
	def __init__(self, branch, hash, testFile, traceDirectory, imageDirectory):
		self.branch = branch
		self.testFile = testFile
		self.blenderplayer = prefixBuildBranchDir + self.branch + "/bin/blenderplayer"
		self.traceDirectory = traceDirectory
		self.traceFile = traceDirectory + hash + "_" + self.testFile.replace(homeDir, "").replace("/", "_") + ".trace"
		self.imageDirectory = imageDirectory

	def trace(self):
		try:
			mkdir("-p", self.traceDirectory)
			apitrace("trace", "-o", self.traceFile, self.blenderplayer, "-p", traceMainScript, self.testFile, _out=debugSh)
		except ErrorReturnCode:
			msgerr("Failed trace branch {} blenderplayer".format(self.branch))
			return False
		else:
			msgstat("Sucess trace branch {} blenderplayer".format(self.branch))

	def dump(self):
		try:
			mkdir("-p", self.imageDirectory)
			apitrace("dump-images", "--call-nos=no", "-o", self.imageDirectory, self.traceFile)
			msgstat("Success dump branch {}".format(self.branch))
		except:
			msgerr("Failed dump branch {}".format(self.branch))

	def getImages(self):
		images = glob(self.imageDirectory + "*.png")
		images.sort()
		return images

class BranchTrace:
	def __init__(self, branch, hash):
		self.branch = branch
		self.hash = hash
		self.traceDirectory = traceDir + self.branch + "/"
		self.imageDirectory = imageDir + self.branch + "_" + self.hash + "/"

	def run(self, testFile):
		return FileTrace(self.branch, self.hash, testFile, self.traceDirectory, self.imageDirectory)


def compareImages(images1, images2):
	if len(images1) == 0 or len(images2) == 0:
		msgerr("Invalid image lists to compare")
		return

	minsize = min(len(images1), len(images2))

	images1 = images1[0:minsize]
	images2 = images2[0:minsize]

	diffs = []
	for image1, image2 in zip(images1, images2):
		msgcmd("Compare image {} and {}".format(image1, image2))

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
	branches = (BranchTrace("master", "0000"), BranchTrace("ge_blender_glsl", "0000"))
	images = []
	for branch in branches:
		filetrace = branch.run(testFiles + "Render/Material/Color/meshColor.blend")
		if not "--no-trace" in sys.argv:
			filetrace.trace()
		if not "--no-dump" in sys.argv:
			filetrace.dump()
		images.append(filetrace.getImages())

	print(images)

	diffs = compareImages(images[0], images[1])

	for i, diff in enumerate(diffs):
		print("Images {} and {} has difference of {}".format(images[0][i], images[1][i], diff))
