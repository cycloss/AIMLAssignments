import numpy as np
import matplotlib.pyplot as plt
from mathFuncs import computePDF


class PDFGrapher:
    @staticmethod
    def addPDFToPlot(variance: float, mean: float):
        # four standard deviations from left and right
        stdDeviation = variance**0.5
        extent = stdDeviation * 4
        xs = np.linspace(mean - extent, mean + extent, 100)
        ys = [computePDF(x, variance, mean) for x in xs]
        plt.plot(xs, ys)

    @staticmethod
    def showPlot():
        plt.show()