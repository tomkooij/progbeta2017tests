import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exact(test):
	def testMethod():
		result = lib.outputOf(_fileName).split("\n")[0].strip()
		testResult = assertlib.exact(result, "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]")
		return testResult, result
	test.test = testMethod
	
	test.description = lambda : "print een lijst van alle priem getallen onder 100"

@t.test(1)
def numberOfPrimes(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName).split("\n")[1].strip(), "25")
	test.description = lambda : "print het correcte aantal priemgetallen"