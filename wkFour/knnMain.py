# xnew = {gender=female, age=26, BMI=20, home_city=birmingham}
# output attribute = illness

# what is the distance between xnew and each point
# what class is xnew predicted to be if k = 3

# for each attribute (dimension), calculate the distance
# for categorical, 1 if same, 0 if different
# compute euclidean distance:
# root((xi1 - xj1)^2 + ... + (xin - xjn)^2)
# must also normalise xi and xj so that xi - xj will be between 0 and 1 inclusive
# for a given dimension p:
# example i's p dimension - p dimension’s minimum / p dimension’s maximum - p dimension’s minimum

import pandas as pd
import math
from collections import Counter


def normalise(point, dimensionMin, dimensionMax):
    return (point - dimensionMin) / (dimensionMax - dimensionMin)


df = pd.read_csv('knnData.csv')
attributes = df.drop('illness', axis=1).columns
xnew = {'gender': 'female', 'age': 26, 'bmi': 20, 'home city': 'birmingham'}

ageMin = min(df['age'].min(), xnew['age'])
ageMax = max(df['age'].max(), xnew['age'])
bmiMin = min(df['bmi'].min(), xnew['bmi'])
bmiMax = max(df['bmi'].max(), xnew['age'])

newNormAge = normalise(xnew['age'], ageMin, ageMax)
newNormBmi = normalise(xnew['bmi'], bmiMin, bmiMax)

for i, row in df.iterrows():
    ageNorm = normalise(row['age'], ageMin, ageMax)
    normAgeDiff = newNormAge - ageNorm
    bmiNorm = normalise(row['bmi'], bmiMin, bmiMax)
    normBmiDiff = newNormBmi - bmiNorm
    genderDiff = xnew['gender'] != row['gender']
    cityDiff = xnew['home city'] != row['home city']
    df.loc[i, 'distance'] = math.sqrt(normAgeDiff**2 + normBmiDiff**2 +
                                      genderDiff + cityDiff)

print('Top 3 closest:\n')
top3 = df.sort_values('distance').head(3)
print(top3, '\n')

mostFrequentClass = Counter(top3['illness']).most_common(1)[0][0]
print(f'Illness likely: {mostFrequentClass}')
