import re
import sys

sOriginals = ["hello!", "prOGraMMIng PuZZleS & cOde ____", "helLO, worl_!", "i aM yoUr faTh__.", "Can YOu gUesS tHE ENd oF This ____?", "THe qUICk brown FOx JUMps oVEr the la__ ___.", "RoadS? wHERe we're goinG WE doN't need _____.", "thE greatESt Trick thE DeVIl EVer PUllEd wAs CONvInciNg tHe WorLD h_ ____'_ _____.", "BInar_", "hyPerbolIZ__"]

"""
This function decodes a string, using a modified Bacon's cipher,
as per the rules from:
https://codegolf.stackexchange.com/questions/164647/programming-puzzles-code

"""
def baconize(sOriginal):

	# if the input has no underscore, return it and exit
	if "_" not in sOriginal:
		print(sOriginal)
		return

	# 26 alpha letters
	sDict = "abcdefghijklmnopqrstuvwxyz"

	# create a copy string and remove anything except alphanumeric
	sInputStr = re.sub(r'([^\s\w])+|_', '', sOriginal)

	# split and join the string to remove spaces
	sInputStr = "".join(sInputStr.split())

	# split the string into a list by 5 characters
	lInput = [sInputStr[i:i+5] for i in range(0, len(sInputStr), 5)]

	# remove any leftover items which are shorter than 5 characters
	lInput[:] = [x for x in lInput if len(x) == 5]

	# if the number of underscores and number of items is not equal, remove the last item from the list
	if sOriginal.count("_") != len(lInput):
		lInput = lInput[:-1]

	# turn each item into a binary representation of the index of sDict, then append the character into lCode
	lCode = []
	for item in lInput: # iterate through the items
		b = ""
		for ch in item: # iterate through the characters of each item
			if ch.isupper():
				b += "1"
			else:
				b += "0"
		lCode.append(sDict[int(b, 2)])

	# iterate through the original string, make a copy in sResult and replace underscores with the proper characters
	i = 0
	sResult = ""
	for c in range(0, len(sOriginal)):
		if sOriginal[c] != "_":
			sResult += sOriginal[c]
		else:
			sResult += lCode[i]
			i += 1

	# display the results
	print("Original: ", sOriginal)
	print("Result: ", sResult.lower())

# iterate through the test case items and use the function
for s in sOriginals:
	baconize(s)
	print(" ------ ")
