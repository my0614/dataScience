import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_json('crime.json')
a = input()
df = df[a]
pd.DataFrame(df)

