from typing import List
from vectors import Vector3

import math
# while not converged:
#       cost = 0
#       for example j in observations:
#             cost += ( yj - hw( xj ) ) ^ 2
#             w1 = w1 + α . ( yj - hw( xj ) ) . xj
#             w0 = w0 + α . ( yj - hw( xj ) )
# remember, cost is the 'badness' of the assessment of the current guessed line for the Vector2 trend

# UniVariateLinearSeparableModel


class UVLSModel:

    def __init__(self, dataPoints: List[Vector3], initialW0: float, initialW1: float, initialW2: float, alpha: float, epochs: int):
        self.dataPoints = dataPoints
        self.w0 = initialW0
        self.w1 = initialW1
        self.w2 = initialW2
        self.alpha = alpha
        self.epochs = epochs

    def run(self):
        # run all epochs
        for i in range(self.epochs):
            print(f'Iteration {i + 1}:')
            self.__iterateData()

    def __iterateData(self):
        cost = 0.0
        # run through Vector3 points (a single epoch)
        for point in self.dataPoints:
            # g(X) must be calculated ONLY ONCE during this update stage
            hypothesis = self.__applySigmoid(
                self.w0 + self.w1 * point.x1 + self.w2 * point.x2)

            costPenalty = self.__calculateCost(point.y, hypothesis)
            # update cost
            cost += costPenalty

            # update w0
            self.w0 = self.w0 + self.alpha * (point.y - hypothesis)
            # update w1
            self.w1 = self.w1 + self.alpha * (point.y - hypothesis) * point.x1
            # update w2
            self.w2 = self.w2 + self.alpha * (point.y - hypothesis) * point.x2

        # print values after every epoch
        print(
            f'Cost: {cost / len(self.dataPoints)}, w0: {self.w0}, w1: {self.w1}, w2: {self.w2}')

    @staticmethod
    def __applySigmoid(z: float):
        return 1 / (1 + math.exp(-z))

    # actual is y, must be either 0 or 1
    @staticmethod
    def __calculateCost(actual: float, hypothesis: float):
        if actual not in [0, 1]:
            raise ValueError('Y must be either 0 or 1')
        temp = actual * math.log(hypothesis) + \
            (1 - actual) * math.log(1 - hypothesis)
        return -temp


# multivariate, so x1 and x2 are the independent variables in vector X, and y is the actual classification (1 it was the thing, 0 it wasn't)
dataPoints = [Vector3(1, 1, 0), Vector3(2, 2, 0), Vector3(0.3, 1.2, 0), Vector3(0.6, 0.8, 0), Vector3(1.2, 1, 0), Vector3(1.3, 1, 0), Vector3(1.8, 2, 0), Vector3(
    1.5, 1.4, 0), Vector3(3, 3, 1), Vector3(4, 4, 1), Vector3(3.1, 3.3, 1), Vector3(3.6, 3.8, 1), Vector3(3.8, 2.1, 1), Vector3(3.5, 2.2, 1), Vector3(3.25, 2.8, 1)]

model = UVLSModel(dataPoints, 0, 0, 0, 0.5, 10)
model.run()
