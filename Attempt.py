import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nums = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
nums = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
plt.hist(nums, bins=10, range=None, density=False, weights=None,
         cumulative=False, bottom=None, histtype='bar', align='mid',
         orientation='vertical', rwidth=None, log=False, color=None,
         label=None, stacked=False)
