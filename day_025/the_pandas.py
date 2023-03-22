import pandas as pd
import numpy as np

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)