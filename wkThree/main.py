import csv
from data import Data
from mathFuncs import *
from graphing import PDFGrapher
# indepVars = {height=154, Wear_Glasses=Yes, Favourite_Music_Genre=Pop}, what is the most probable output class
# output classes are toddler, child, teenager, young adult, adult, elderly

# height needs a pdf for probabilities
# others can use laplace smoothed frequency tables
# output for columns, input for rows, each table has a different input

# compute:
# p(Toddler | indepVars)
# p(Child | indepVars)
# p(Teenager | indepVars)
# p(Young Adult | indepVars)
# p(Adult | indepVars)
# p(Elderly | indepVars)

# most likely is answer

reader = csv.reader(open('wk3Data.csv', 'r'))
next(reader)  # remove table headers
data = [Data(row[0], row[1], row[2], row[3]) for row in reader]

grouped = Data.groupData(data)


def calculateGroupProbs(data: list):
    groupCounts = dict()
    for dataPoint in data:
        groupCounts[dataPoint.ageGrp] = groupCounts.get(dataPoint.ageGrp,
                                                        0) + 1
    total = len(data)
    for k, v in groupCounts.items():
        groupCounts[k] = v / total
    return groupCounts


# calculate height pdf for each class
def calculateHeightProbs(grouped: dict, height: float) -> dict:
    retDict = dict()
    for className, dataPoints in grouped.items():
        heights = list(map(lambda item: item.height, dataPoints))
        mean = computeMean(heights)
        variance = computeVariance(heights, mean)
        PDFGrapher.addPDFToPlot(variance, mean)
        probForHeight = computePDF(height, variance, mean)
        print(
            f'{className:11} mean = {mean:<7.2f} variance = {variance:<7.2f} P(154) = {probForHeight:.5f}'
        )
        retDict[className] = probForHeight
    PDFGrapher.showPlot()
    return retDict


# calculate probabilities of wearing glasses for each class
def calculateGlassesProbs(groupedData: dict[str, Data], glasses: bool) -> dict:
    retDict = dict()
    for ageGrp, group in groupedData.items():
        # calculate laplace smoothed for yes and no
        glassesYes = sum([1 for point in group if point.glasses]) + 1
        glassesNo = sum([1 for point in group if not point.glasses]) + 1
        print(f'{ageGrp} glasses yes: {glassesYes}, glasses no: {glassesNo}')
        # given ageGrp, calculate probability of yes
        pYes = glassesYes / (glassesNo + glassesYes)
        retDict[ageGrp] = pYes if glasses else 1 - pYes

    return retDict


def calculateMusicProbs(grouped: dict, genre: str) -> dict:
    retDict = dict()
    for ageGrp, dataPoints in grouped.items():
        # calculate laplace smoothed for all genres
        probDict = {'Classical': 1, 'Country': 1, 'Pop': 1}
        for dataPoint in dataPoints:
            probDict[dataPoint.favMusic] = probDict.get(dataPoint.favMusic,
                                                        0) + 1
        total = sum([v for _, v in probDict.items()])
        probSelected = probDict[genre] / total
        retDict[ageGrp] = probSelected
    return retDict


# return alpha and each of the probabilities
def calculateCombinedProbabilities(groupProbs, heightProbs, glassesProbs,
                                   musicProbs) -> dict:
    retDict = dict()
    beta = 0
    for ageGrp in Data.outClasses:
        groupProb = groupProbs[ageGrp]
        heightProb = heightProbs[ageGrp]
        glassesProb = glassesProbs[ageGrp]
        musicProb = musicProbs[ageGrp]
        # p(ageGrp | independentVars) =
        pAgeGrp = groupProb * heightProb * glassesProb * musicProb
        retDict[ageGrp] = pAgeGrp
        beta += pAgeGrp

    return retDict, 1 / beta


def calculateRelativeProbs(combinedProbs: dict, alpha: float) -> dict:
    retDict = dict()
    for k, v in combinedProbs.items():
        retDict[k] = v * alpha
    return retDict


groupProbabilities = calculateGroupProbs(data)
heightProbs = calculateHeightProbs(grouped, 154)
glassesProbs = calculateGlassesProbs(grouped, True)
musicProbs = calculateMusicProbs(grouped, 'Pop')

combinedProbs, alpha = calculateCombinedProbabilities(groupProbabilities,
                                                      heightProbs,
                                                      glassesProbs, musicProbs)
print('Combined probs:')
print(combinedProbs)
print(alpha)

#check relative probability adds to 1
print(sum([prob * alpha for k_, prob in combinedProbs.items()]))
# apply bayes to the calculated probabilities of each class and pick the most likely

relativeProbs = calculateRelativeProbs(combinedProbs, alpha)

for k, v in relativeProbs.items():
    print(f'{k:11}: {v:.5f}')