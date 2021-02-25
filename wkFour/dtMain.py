import pandas as pd
from dtFuncs import *

df = pd.read_csv('dtData.csv')
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
    # calculate entropy sum of attribute's split values groups
    entropySum = 0
    for _, group in grouped:
        # InfoGain(examples, A) = Entropy(examples) - SUM((len(examples_vi) / len(examples) * Entropy(examples_vi))
        weight = len(group) / len(selected)
        entropySum += weight * calculateEntropy(group[output].values)
    print(f'Entropy gain for {attr}: {currentEntropy - entropySum:.5f}')
    # subtract from current entropy to get resulting gain from split on attribute
