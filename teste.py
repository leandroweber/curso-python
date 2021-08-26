
import pandas as pd
df = pd.DataFrame({"A": [10, 20, -5, -10, 20],
                   "B": [10, 20, -5, -10, 89]}
                  )

df['C'] = df["A"] + df["B"]
print(df)
