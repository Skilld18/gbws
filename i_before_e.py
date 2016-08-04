#!/usr/bin/env python

#Question: Is the ie before e thing actually useful?
#Answer: Kind of, Depending on the word list used I got as low as 65% correct and as high as 85% 
#but that is nowhere near good enough to be a "rule"
#These number would be improved by properly implementing rule 3 "Or when sounded as "EYE" or "AY" as in Einstein and weigh"
#But I'm not sure that should really count.
#Just a cursory look at the list of words shows that alot of the "rulebreakers" were loan words especially german words like zeitgeist
#Which manages breaks the rule twice


#Use i before es
#Except after c
#Or when sounded as "EYE" or "AY" as in Einstein and weigh.	
#Neither, weird, foreign, leisure, Seize, forfeit, and height Are Exceptions spelled right	
#But don't let the C-I-E-N words get you uptight!	

correct = 0
incorrect = 0

with open("wordlist.txt") as f:
    wordlist = f.readlines()

for word in wordlist:
	word = word.lower()
	e4 = ["Neither", "weird", "foreign", "leisure", "Seize", "forfeit", "height"]
	e3 = ["Einstein, weight"]
	#5
	if "cien" in word:
		correct += 1
		continue
	elif "cein" in word:
		incorrect += 1
		print(word)
		continue
	#4
	for e in e4:
		if word in e4:
			correct += 1
			continue

	#TODO: get phonetic symbol list
	#3 The rest of this is predicated on extra information which the poem does not supply (and is hard to code)
	if word in e3:
		correct += 1
		continue

	#2
	if "cei" in word:
		correct += 1
		continue
	elif "cie" in word:
		incorrect += 1
		print(word)
		continue

	#1
	if "ie" in word:
		correct += 1
		continue
	elif "ei" in word:
		incorrect += 1
		print(word)
		continue

print(correct/float(correct + incorrect))
print(correct + incorrect)
