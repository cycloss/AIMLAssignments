import pandas as pd
import numpy as np
import math
from collections import Counter


# Entropy(examples) = - (pc_1 * log2(p_c1) + p_c2 * log2(p_c2) + ... + p_ck * log2(p_ck))
# parameter outputList is a list of the different output values for the current data set
# since the input values are yes or no, these are strings (could be converted to bools)
def calculateEntropy(outputList: list[str]) -> float:
    # output class probabilities
    probabilities = [v / len(outputList) for v in Counter(outputList).values()]
    return -sum(0 if p == 0 else p * math.log(p, 2) for p in probabilities)


# def calculateEntropyGain(groupedata: pd.DataFrame, currentEntropy: float) -> float:

# calculate resulting entropy of resulting sets

df = pd.read_csv('data.csv')
# print(df)

attributes = [
    'Gender', 'Smoke', 'Home City', 'Life Stage', 'BMI Category', 'Activeness'
]
output = 'Illness'

currentEntropy = calculateEntropy(df[output].values)
print(f'Current entropy: {currentEntropy}\n')

# need to select each attribute and output, and then calculate the resulting gain using each of the resulting sets from the attribute values
for attr in attributes:
    # selects the target attribute and output column
    selected = df[[attr, output]]
    # for selected attribute split it into groups corresponding to the different attribut values
    grouped = selected.groupby(attr)
    # InfoGain(examples, A) = Entropy(examples) - SUM((len(examples_vi) / len(examples) * Entropy(examples_vi))
    # calculate entropy sum of attribute's split values groups
    entropySum = 0
    for _, group in grouped:
        weight = len(group) / len(selected)
        entropySum += weight * calculateEntropy(group[output].values)
    print(f'Entropy gain for {attr}: {currentEntropy - entropySum:.5f}')
    # subtract from current entropy to get resulting gain from split on attribute
