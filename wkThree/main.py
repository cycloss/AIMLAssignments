import csv
from data import Data
from mathFuncs import *
from graphing import PDFGrapher
# indepVars = {height=154, Wear_Glasses=Yes, Favourite_Music_Genre=Pop}, what is the most probable output class
# output classes are toddler, child, teenager, young adult, adult, elderly

# height needs a pdf for probabilities
# others can use laplace smoothed frequency tables

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

# calculate height pdf for each class
for className, dataPoints in grouped.items():
    heights = list(map(lambda item: item.height, dataPoints))
    mean = computeMean(heights)
    variance = computeVariance(heights, mean)
    PDFGrapher.addPDFToPlot(variance, mean)
    print(
        f'{className} stats: mean = {mean:.2f}, variance = {variance:.2f}, 154 probability: {computePDF(154, variance, mean):.5f}'
    )

PDFGrapher.showPlot()
