import pickle
import sys

filename = sys.argv[1]
category = sys.argv[2]

def computeCategory(category, profiles):
	maxtime = 0.0
	mintime = 100000000.0
	averagetime = 0.0
	averageinfluence = 0.0
	for item in profiles:
		profile = item[1]
		pair = profile[category + ":"]
		time = pair[0]
		influence = pair[1]

		if time < mintime:
			mintime = time
		if time > maxtime:
			maxtime = time

		averagetime += time
		averageinfluence += influence

	return (averagetime / len(profiles), averageinfluence / len(profiles), mintime, maxtime)

def printCategory(category, results):
	print("Category:", category)
	print("\t Average time:\t\t", results[0], " ms")
	print("\t Average influence:\t", results[1], " %")
	print("\t Min time:\t\t", results[2], " ms")
	print("\t Max time:\t\t", results[3], " ms")

with open(filename, "rb") as file:
	profiles = pickle.load(file)

	results = computeCategory(category, profiles)
	printCategory(category, results)
