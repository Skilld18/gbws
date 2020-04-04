#!/usr/bin/python


from string import ascii_lowercase


with open("wordlist.txt") as f:
    wordlist = f.readlines()

def is_word(word):
    global wordlist
    return word + "\n" in wordlist

def swap(word):
    for i in range(len(word)-1):
        c = word[i]
        yield word[:i] + word[i + 1] + c + word[i+2:]

def insert(word):
    for i in range(len(word)+1):
        for c in ascii_lowercase:
            yield word[:i] + c + word[i:]

def delete(word):
    for i in range(len(word)):
        yield word[0:i] + word[i+1:]

def replace(word):
    for i in range(len(word)):
        for c in ascii_lowercase:
            yield word[0:i] + c + word[i+1:]

def valid_op_type(word):
    yield swap(word)
    yield insert(word)
    yield delete(word)
    yield replace(word)


def hamming(a):
    for opt in valid_op_type(a):
        for op in opt:
            yield op


possible = set()
for word in hamming("make"):
    if is_word(word):
        possible.add(word)
print(possible)
