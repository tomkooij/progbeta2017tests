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
		test_distance = (assertlib.numberOnLine(10.86, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.02) or assertlib.numberOnLine(10860, lib.getLine(lib.outputOf(_fileName), 0), deviation = 20))
			

		return test_distance

	test.test = testMethode
	test.description = lambda : "print de correcte afgelegde afstand"
	test.timeout = lambda : 60
