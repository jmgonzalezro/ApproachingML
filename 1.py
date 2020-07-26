import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import datasets
from sklearn import manifold

# %matplotlib inline
data = datasets.fetch_openml(
    "mnist_784",
    version = 1,
    return_X_y=True
)
pixel_values, targets = data
targets = targets.astype(int)















