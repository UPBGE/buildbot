from common import *
from print import *
from sh import apitrace

def dumpImage(trace, ):
	try:
		apitrace("dump-images", "-o", directory, trace)
		msgstat("Success dump")
	except:
		msgerr("Failed dump")
