import math


def computeMean(vals: list[float]) -> float:
    return sum(vals) / len(vals)


def computeVariance(vals: list[float], mean: float) -> float:
    meanSqrErrSum = 0
    for val in vals:
        meanSqrErrSum += (val - mean)**2
    return meanSqrErrSum * (1 / (len(vals) - 1))


def computePDF(inputVal: float, variance: float, mean: float) -> float:
    eExponent = -(inputVal - mean)**2 / (2 * variance)
    eVal = math.exp(eExponent)
    fraction = 1 / (2 * variance * math.pi)**0.5
    return fraction * eVal