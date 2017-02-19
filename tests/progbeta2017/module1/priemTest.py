import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def isPrime37(test):
	test.test = lambda : not assertlib.contains(lib.getLine(lib.outputOf(_fileName, [37]), 0), "geen")
	test.description = lambda : "37 is een priemgetal"

@t.test(10)
def isPrime36(test):
	test.test = lambda : assertlib.contains(lib.getLine(lib.outputOf(_fileName, [36]), 0), "geen")
	test.description = lambda : "36 is geen priemgetal"

@t.test(20)
def isPrime7349(test):
	test.test = lambda : not assertlib.contains(lib.getLine(lib.outputOf(_fileName, [7349]), 0), "geen")
	test.description = lambda : "7349 is een priemgetal"
