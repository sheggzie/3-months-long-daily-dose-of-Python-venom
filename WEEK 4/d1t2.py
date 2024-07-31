# Create a simple DataFrame using the pandas library.

import pandas as pd

data = {
    "names": ["john", "doe", "james", "jenny"],
    "city": ["lagos", "oyo", "ibadan", "togo"],
    "id": [5000, 6000, 450, 900]
}

df = pd.DataFrame(data)

print(df.describe())

print(df.info())

