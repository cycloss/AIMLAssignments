import math
import pandas as pd
from collections import Counter


# Entropy(examples) = - (pc_1 * log2(p_c1) + p_c2 * log2(p_c2) + ... + p_ck * log2(p_ck))
# parameter outputList is a list of the different output values for the current data set
# since the input values are yes or no, these are strings (could be converted to bools)
def calculateEntropy(outputList: list[str]) -> float:
    # output class probabilities
    probabilities = [v / len(outputList) for v in Counter(outputList).values()]
    return -sum(0 if p == 0 else p * math.log(p, 2) for p in probabilities)