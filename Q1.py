import numpy as np
import pandas as pd

df = pd.read_csv("country_vaccination_stats.csv")

replacements = df[["country","daily_vaccinations"]].groupby("country").min()

replacements = replacements.fillna(0)

df['daily_vaccinations'] = df.apply(
    lambda row: replacements.loc[row["country"]][0] if np.isnan(row['daily_vaccinations']) else row['daily_vaccinations'],
    axis=1
)