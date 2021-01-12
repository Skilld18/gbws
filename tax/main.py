import matplotlib.pyplot as plt

from data import *
from bracket import *
bracket_list = []
clean_bracket_list = []
for b in canadian_tax_brackets:
    bracket_list.append(Bracket(*b))

for b in cleaner_canadian_tax_brackets:
    clean_bracket_list.append(Bracket(*b))

bracket_list = sorted(bracket_list)
if not Bracket.valid_brackets(bracket_list):
    exit(1)
clean_bracket_list = sorted(clean_bracket_list)
if not Bracket.valid_brackets(clean_bracket_list):
    exit(1)

data = []
clean_data = []
for i in range(0, 300000, 1):
    tax_paid = Bracket.calc_brackets(i, bracket_list)
    clean_tax_paid = Bracket.calc_brackets(i, bracket_list)
    data.append(tax_paid)
    clean_tax_paid = Bracket.calc_brackets(i, clean_bracket_list)
    clean_data.append(clean_tax_paid)

plt.plot(data)
plt.plot(clean_data)
plt.axvline(49020)
plt.axvline(98040)
plt.axvline(151978)
plt.axvline(216511)

plt.plot(data)

plt.show()
