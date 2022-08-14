import itertools
with open("wordlist.txt") as f:
    words = f.readlines()
words = map(lambda x:x.lower().strip("\n"), words)



def is_five_letters(word):
    return len(word) == 5


def is_unique(words):
    return len(set("".join(words))) == len(list("".join(words)))


words = filter(is_five_letters, words)
words = itertools.combinations(words, 4)
words = filter(is_unique, words)

for word in words:
    print(word)
