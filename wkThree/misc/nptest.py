import matplotlib.pyplot as plt
import numpy as np

# linspace numbers are inclusive
nums = np.linspace(0, 1, 11)
print(nums)

# 3rd num is step
nums2 = np.arange(0, 10, 0.5)
print(nums2)

# a range last number is exclusive
nums3 = np.arange(5, 8)
print(nums3)

normal = np.random.normal(size=10)
print(normal)

ys = [x**2 for x in nums2]
# now can translate ys list using np array
print(ys)
ys2 = np.array(ys) * 2
print(ys2)

print(np.int8(255))
print(np.uint8(255))