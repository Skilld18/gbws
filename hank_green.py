#!/usr/bin/python3


#An Absolutely remarkably thing
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from nltk.corpus import wordnet as wn
import re

def ends_in_ly(word):
    return word[-2:] == "ly"


def nsyl(word):
    d = cmudict.dict()
    try:
        return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]
    except:
        return -1


def starts_with_vowel_sound(word, pronunciations=cmudict.dict()):
    for syllables in pronunciations.get(word, []):
        return syllables[0][-1].isdigit()  # use only the first one

def a_or_an(word):
    return "an" if starts_with_vowel_sound(word) else "a"


def get_title(adv, adj, noun):
    return a_or_an(adv) + " " + adv + " " + adj + " " + noun
    

def get_word_type(t):
    for synset in list(wn.all_synsets(t)):
        word = re.search("^[^.]*", synset.name()).group()
        if t == wn.ADV and (not ends_in_ly(word) or "_" in word or nsyl(word) < 3):
            continue
        yield word


advs = get_word_type(wn.ADV)
adjs = get_word_type(wn.ADJ)
nouns = get_word_type(wn.NOUN)



while True:
    adv = next(advs)
    adj = next(adjs)
    noun = next(nouns)

    #todo CAPS
    print(get_title(adv, adj, noun))



