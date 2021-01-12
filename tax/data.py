import sys


ALL_THE_MONEY = sys.maxsize
MAX = ALL_THE_MONEY
BROKE = 0
MEAN = -1
MEDIAN = -1
RICHEST_PERSON_IN_CANADA = 39000000
ME = -1

CANADIAN_INCOMES = range(BROKE, RICHEST_PERSON_IN_CANADA, 1000)

canadian_tax_brackets = [
    (     0,  49020, 0.15), # noqa
    ( 49020,  98040, 0.205),# noqa
    ( 98040, 151978, 0.26), # noqa
    (151978, 216511, 0.29), # noqa
    (216511,    MAX, 0.33)  # noqa
]

cleaner_canadian_tax_brackets = [
    (     0,  50000, 0.15), # noqa
    ( 50000, 100000, 0.20), # noqa
    (100000, 150000, 0.25), # noqa
    (150000, 200000, 0.30), # noqa
    (200000,    MAX, 0.35)  # noqa
]
