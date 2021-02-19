from typing import List
from vectors import Vector2

# while not converged:
#       cost = 0
#       for example j in observations:
#             cost += ( yj - hw( xj ) ) ^ 2
#             w1 = w1 + α . ( yj - hw( xj ) ) . xj
#             w0 = w0 + α . ( yj - hw( xj ) )
# remember, cost is the 'badness' of the assessment of the current guessed line for the Vector2 trend

# UniVariateLinearModel


class UVLModel:

    def __init__(self, dataPoints: List[Vector2], initialW0: float, initialW1: float, alpha: float, epochs: int):
        self.dataPoints = dataPoints
        self.w0 = initialW0
        self.w1 = initialW1
        self.alpha = alpha
        self.epochs = epochs

    def run(self):
        # run all epochs
        for i in range(self.epochs):
            print(f'Iteration {i + 1}:')
            self.__iterateData()

    def __iterateData(self):
        cost = 0.0
        # run through Vector2 points (a single epoch)
        for Vector2Point in self.dataPoints:
            # h_w(x) must be calculated ONLY ONCE during this update stage
            l1Cost = Vector2Point.y - (self.w0 + self.w1 * Vector2Point.x)
            l2Cost = l1Cost ** 2
            # update cost
            cost += l2Cost
            # update w0
            self.w0 = self.w0 + self.alpha * l1Cost
            # update w1
            self.w1 = self.w1 + self.alpha * l1Cost * Vector2Point.x

        # print values after every epoch
        print(
            f'Cost: {cost / len(self.dataPoints)}, w1: {self.w1}, w0: {self.w0}')


Vector2Points = [Vector2(1, 1), Vector2(2, 5), Vector2(3, 11)]
m1 = UVLModel(Vector2Points, 1, 1, 1, 1)
m1.run()

Vector2Points2 = [Vector2(1, 12)]
m2 = UVLModel(Vector2Points2, 1, 2, 0.001, 1)
m2.run()
