#!/usr/bin/python3


from random import randint
import itertools


def nice(last):
    return 1

def mean(last):
    return 0

def random(last):
    return randint(0,1)

def nice_forgiving_retaliatory(last):
    if last == None:
        return 1
    return last

def scoring(a, b, aplay, bplay):
    global score
    collaberate = 5
    assualt = 10
    defect = 0
    if aplay == 1 and bplay == 1:
        score[str(a)] += collaberate
        score[str(b)] += collaberate
    elif aplay == 0 and bplay == 0:
        score[str(a)] += defect
        score[str(b)] += defect
    elif aplay == 0 and bplay == 1:
        score[str(a)] += assualt
    elif aplay == 1 and bplay == 0:
        score[str(b)] += assualt


competitors = [nice, mean, random, nice_forgiving_retaliatory]
# competitors = [mean, nice_forgiving_retaliatory]

crosstable = list(itertools.combinations_with_replacement(competitors, 2))
score = {str(nice): 0, str(mean): 0, str(random): 0, str(nice_forgiving_retaliatory): 0}
for i in crosstable:
    last = [None, None]
    for j in range(5):
        aplay = i[0](last[1])
        bplay = i[1](last[0])
        last[0] = aplay
        last[1] = bplay
        print(i, aplay, bplay)
        scoring(i[0], i[1], aplay, bplay)
print(score)
