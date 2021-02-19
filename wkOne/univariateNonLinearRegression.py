from typing import List
from vectors import Vector2

# j is the jth Vector2 point set

# while epochs remaining:
#       cost = 0
#       for example j in observations:
#             cost += ( yj - hw( xj ) ) ^ 2 #l2 loss
#             w0 = w0 + α . ( yj - hw( xj ) )
#             w1 = w1 + α . ( yj - hw( xj ) ) . xj
# 	          …….
# 	          wn = wn + α . ( yj - hw( xj ) ) . xj^n

# UniVariateNonLinearModel


class UVNLModel:

    def __init__(self, dataPoints: List[Vector2], initialW0: float, initialW1: float, initialW2: float, alpha: float, epochs: int):
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
        # run through Vector2 points (a single epoch)
        for Vector2Point in self.dataPoints:
            # h_w(x) or l1cost must be calculated ONLY ONCE during this update stage
            l1Cost = Vector2Point.y - \
                (self.w0 + self.w1 * Vector2Point.x + self.w2 * Vector2Point.x ** 2)
            l2Cost = l1Cost ** 2
            # update cost
            cost += l2Cost
            # update w0
            self.w0 = self.w0 + self.alpha * l1Cost
            # update w1
            self.w1 = self.w1 + self.alpha * l1Cost * Vector2Point.x
            # update w2
            self.w2 = self.w2 + self.alpha * \
                l1Cost * Vector2Point.x ** 2

        # print values after every epoch
        print(
            f'Cost: {cost / len(self.dataPoints)}, w0: {self.w0}, w1: {self.w1}, w2: {self.w2}')


Vector2Points = [Vector2(-10, 91), Vector2(-3, 7), Vector2(0, 1), Vector2(1, 3),
                 Vector2(2, 7), Vector2(3, 13), Vector2(4, 21), Vector2(10, 111)]
m1 = UVNLModel(Vector2Points, 0, 0, 0, 0.000001, 100)
m1.run()
