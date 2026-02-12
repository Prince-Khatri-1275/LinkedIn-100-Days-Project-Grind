# LR Data Generation

import os
import numpy as np
import pandas as pd 

sample_size = 10000

slope = 5.7
intercept = -5.2

x = np.random.randint(-1024, 1023, sample_size) / 1024
y = x * slope + intercept + np.random.uniform()

df = pd.DataFrame([x, y], index=["x", "y"]).T
df.to_csv(os.path.join("Day 1", "datasets", "lr_data.csv"), index=False)