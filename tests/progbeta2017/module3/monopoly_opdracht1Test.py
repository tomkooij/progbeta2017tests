import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re
import os

@t.test(0)
def hasworp_met_twee_dobbelstenen(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "worp_met_twee_dobbelstenen")
	test.description = lambda : "definieert de functie worp_met_twee_dobbelstenen"


@t.passed(hasworp_met_twee_dobbelstenen)
@t.test(10)
def correctDice(test):
	test.test = lambda : assertlib.between(lib.getFunction("worp_met_twee_dobbelstenen", _fileName)(), 2, 12)
	test.description = lambda : "returnt een correcte waarde voor een worp van twee dobbelstenen"
	

@t.passed(correctDice)
@t.test(20)
def hassimuleer_potjeAndsimuleer_groot_aantal_potjes_Monopoly(test):
	def testMethod():
			test_potje = assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_potje_Monopoly")
			test_groot_aantal_potjes = assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_groot_aantal_potjes_Monopoly")
			info = ""
			if not test_potje:
				info = "de functie simuleer_potje_Monopoly is nog niet gedefinieerd"
			elif not test_groot_aantal_potjes:
				info = "de functie simuleer_potje_Monopoly is gedefinieerd :) \n  - de functie simuleer_groot_aantal_potjes_Monopoly nog niet"
			return lambda : test_potje and test_groot_aantal_potjes, info
	
	test.test = testMethod
	test.description = lambda : "definieert de functie simuleer_potje_Monopoly en simuleer_groot_aantal_potjes_Monopoly"


@t.passed(hassimuleer_potjeAndsimuleer_groot_aantal_potjes_Monopoly)
@t.test(30)
def correctAverageTrump(test):

	def try_run():
		try:	
			testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)()
			test.success = lambda info : "De code werkt zonder startgeld, je kunt nu startgeld invoeren!"
			return testInput
		except:
			testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000000)
			return testInput


	test.test = lambda : assertlib.between(try_run(), 145, 149)
	test.description = lambda : "Monopoly werkt in Trump-Mode"

@t.passed(correctAverageTrump)
@t.test(40)
def correctAverageStartgeld(test):

	def try_run():
		try:
			return lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1500)
		except:
			return False

	test.test = lambda : assertlib.between(try_run(), 184, 189)
	test.description = lambda : "Monopoly werkt met 1500 euro startgeld"





