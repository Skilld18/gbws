import sys


class Bracket:

    def __init__(self, minimum, maximum, rate):
        if minimum >= maximum:
            raise ValueError("min > max")
        self.minimum = minimum
        self.maximum = maximum
        self.rate = rate

    def __str__(self):
        return str(self.minimum).rjust(14) + " <= income < " + \
               str(self.maximum).rjust(14) + " taxed at " + str(self.rate)

    def taxable(self, income):
        if self.minimum > income:
            return 0
        upper_bound = min(self.maximum, income)
        return upper_bound - self.minimum

    def apply(self, income):
        if self.maximum - self.minimum < income:
            raise ValueError("Income out of bounds")
        return round(income * self.rate)

    def calc_bracket(self, income):
        return self.apply(self.taxable(income))

    def __lt__(self, other):
        return self.minimum < other.minimum

    @staticmethod
    def valid_brackets(bracket_list):
        if bracket_list[0].minimum != 0:
            raise ValueError("Doesn't start at 0")
        if bracket_list[-1].maximum != sys.maxsize:
            raise ValueError("Doesn't end at sys.maxsize")
        if bracket_list != sorted(bracket_list):
            raise ValueError("Unsorted bracket list")
        for i in range(len(bracket_list)-1):
            if bracket_list[i].maximum != bracket_list[i+1].minimum:
                raise ValueError("Gaps in brackets")
        return True

    @staticmethod
    def sort_brackets(bracket_list):
        return sorted(bracket_list)

    @staticmethod
    def calc_brackets(income, bracket_list):
        Bracket.valid_brackets(bracket_list)
        total = 0
        for bracket in bracket_list:
            total += bracket.calc_bracket(income)
        return total
    minimum = -1
    maximum = -1
    rate = -1
