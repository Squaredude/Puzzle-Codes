import re
import sys

sOriginals = ["hello!", "prOGraMMIng PuZZleS & cOde ____", "helLO, worl_!", "i aM yoUr faTh__.", "Can YOu gUesS tHE ENd oF This ____?", "THe qUICk brown FOx JUMps oVEr the la__ ___.", "RoadS? wHERe we're goinG WE doN't need _____.", "thE greatESt Trick thE DeVIl EVer PUllEd wAs CONvInciNg tHe WorLD h_ ____'_ _____.", "BInar_", "hyPerbolIZ__"]

def baconize(sOriginal):
	if "_" not in sOriginal:
		print(sOriginal)
		return

	dict = "abcdefghijklmnopqrstuvwxyz"

	sInputStr = re.sub(r'([^\s\w])+|_', '', sOriginal)

	sCodeCount = sOriginal.count("_")

	sInputStr = "".join(sInputStr.split())

	sInputStr.strip()

	lInput = [sInputStr[i:i+5] for i in range(0, len(sInputStr), 5)]

	lInput[:] = [x for x in lInput if len(x) == 5]

	if sCodeCount != len(lInput):
		lInput = lInput[:-1]

	print("Original: ", sOriginal)

	lCode = []
	for item in lInput:
		b = ""
		for ch in item:
			if ch.isupper():
				b += "1"
			else:
				b += "0"
		lCode.append(dict[int(b, 2)])

	i = 0
	sResult = ""
	for c in range(0, len(sOriginal)):
		if sOriginal[c] != "_":
			sResult += sOriginal[c]
		else:
			sResult += lCode[i]
			i += 1

	print("Result: ", sResult.lower())

for s in sOriginals:
	baconize(s)
	print(" ------ ")