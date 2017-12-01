import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib


def before():
	import matplotlib.pyplot as plt
	plt.switch_backend("Agg")
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot as plt
	plt.switch_backend("TkAgg")
	reload(plt)

@t.test(0)
def hassimuleer_groot_aantal_potjes_Monopoly(test):
	def try_run():
		if assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_groot_aantal_potjes_Monopoly"):
			try:	
				testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000000, 1000000)
				return True
			except:
				return False
		return False

	test.test = try_run
	test.fail = lambda info : "zorg dat de functie twee argumenten heeft, startgeld voor speler 1 en startgeld voor speler 2"
	test.description = lambda : "definieert de functie simuleer_potjeAndsimuleer_groot_aanal_potjes_Monopoly met twee argumenten"
	test.timeout = lambda : 40


@t.passed(hassimuleer_groot_aantal_potjes_Monopoly)
@t.test(10)
def correctAverageDiv(test):
	def testMethod():
		outcome = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1500, 1500)
		if assertlib.sameType(outcome, None):
			info = "Zorg er voor dat de functie simuleer_groot_aantal_potjes_Monopoly het verschil in het bezit van straten returnt en alleen deze waarde returnt"
		elif assertlib.between(outcome, 0, 99999999):
			info = "Als speler 1 meer straten heeft dan speler 2 is het verschil negatief"
		else:
			info = "Het verschil is niet erg groot, gemiddeld zelfs minder dan 1 straat"
		return assertlib.between(outcome, -.45, -.15), info

	test.test = testMethod
	test.description = lambda : "Monopoly met twee spelers geeft de het correcte gemiddelde verschil in gekochten straten"
	test.timeout = lambda : 40



@t.passed(correctAverageDiv)
@t.test(20)
def correctAverageDiv(test):
	test.test = lambda : assertlib.numberOnLine(125, lib.getLine(lib.outputOf(_fileName), 0))
	test.description = lambda : "Monopoly met twee spelers vindt het correcte extra startgeld voor speler 2"
	test.timeout = lambda : 40






