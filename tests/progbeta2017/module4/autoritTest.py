import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

# Thanks to Vera Schild!

def before():
	import matplotlib.pyplot as plt
	plt.switch_backend("Agg")
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot as plt
	plt.switch_backend("TkAgg")
	reload(plt)


@t.test(0)
def correctDistance(test):

	def testMethode():
		test_distance = assertlib.numberOnLine(10.86, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.02)
		if assertlib.numberOnLine(10860, lib.getLine(lib.outputOf(_fileName), 0), deviation = 20):
			info = "Zorg dat je de afgelegde afstand in kilometers geeft"

		return test_distance, info

	test.test = testMethod
	test.description = lambda : "print de correcte afgelegde afstand"

# @t.test(1)
# def showsGraph(test):
# 	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
# 	test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"
