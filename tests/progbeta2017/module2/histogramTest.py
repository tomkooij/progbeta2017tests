import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import math


def before():
	import matplotlib.pyplot as plt
	plt.switch_backend("Agg")
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot as plt
	plt.switch_backend("TkAgg")
	reload(plt)



@t.test(0)
def hasSomRandomGetallen(test):
	print _fileName
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "SomRandomGetallen")
	test.description = lambda : "definieert de functie SomRandomGetallen"


@t.passed(hasSomRandomGetallen)
@t.test(10)
def correctBelow40(test):

	tsts = ['40', 'veertig', 'forty']
	test.test = lambda : assertlib.numberOnLine(6, lib.getLine(lib.outputOf(_fileName), 0), deviation = 5) and sum([assertlib.contains(lib.outputOf(_fileName), tst) for tst in tsts])
	test.description = lambda : "print hoe vaak de som minder dan 40 is"

@t.passed(hasSomRandomGetallen)
@t.test(20)
def correctAbove60(test):
	tsts = ['60', 'zestig', 'sixty']
	test.test = lambda : assertlib.numberOnLine(6, lib.getLine(lib.outputOf(_fileName), 1), deviation = 5) and sum([assertlib.contains(lib.outputOf(_fileName), tst) for tst in tsts])
	test.description = lambda : "print hoe vaak de som meer dan 60 is"








