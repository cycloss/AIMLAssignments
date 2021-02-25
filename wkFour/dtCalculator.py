import math
import pandas as pd
from collections import Counter

# alternative object orientated approach


class EntropyCalc:
    def __init__(self, df: pd.DataFrame, attributes: list[str],
                 outputAttr: str):
        self.rawData = df
        self.attributes = attributes
        self.outputAttr = outputAttr

    def calculateEntropySplits(self):
        currentEntropy = self.__calculateEntropy(
            self.rawData[self.outputAttr].values)
        for attr in self.attributes:
            # selects the target attribute and output column
            selected = self.rawData[[attr, self.outputAttr]]
            # for selected attribute split it into groups corresponding to the different attribut values
            grouped = selected.groupby(attr)
            adjustedGroupEntropy = self.__calcAdjustedGroupedEntropy(grouped)
            print(
                f'Entropy gain for {attr}: {currentEntropy - adjustedGroupEntropy:.5f}'
            )

    def __calcAdjustedGroupedEntropy(self, groupedData: pd.DataFrame) -> float:
        entropySum = 0
        for _, group in groupedData:
            # InfoGain(examples, A) = Entropy(examples) - SUM((len(examples_vi) / len(examples) * Entropy(examples_vi))
            weight = len(group) / self.__rawDataLen()
            entropySum += weight * self.__calculateEntropy(
                group[self.outputAttr].values)
        return entropySum

    def __rawDataLen(self):
        return len(self.rawData)

    # Entropy(examples) = - (pc_1 * log2(p_c1) + p_c2 * log2(p_c2) + ... + p_ck * log2(p_ck))
    # parameter outputList is a list of output values for a data set
    def __calculateEntropy(self, outputList: list[str]) -> float:
        # output class probabilities
        probabilities = [
            v / len(outputList) for v in Counter(outputList).values()
        ]
        return -sum(0 if p == 0 else p * math.log(p, 2) for p in probabilities)


df = pd.read_csv('dtData.csv')
# print(df)

attributes = [
    'Gender', 'Smoke', 'Home City', 'Life Stage', 'BMI Category', 'Activeness'
]
output = 'Illness'

calculator = EntropyCalc(df, attributes, output)
calculator.calculateEntropySplits()