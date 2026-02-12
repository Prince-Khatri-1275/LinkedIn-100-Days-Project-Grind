import os
import pandas as pd
import LinearRegression as lr

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "datasets", "lr_data.csv"))
X, Y = df["x"].to_list(), df["y"].to_list()

m, c = lr.process(X, Y, learning_rate=0.001, epochs=320, batch_size=32, verbose=1)

print(m, c)