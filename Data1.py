import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Import Data from CSV
df = pd.read_csv('https://raw.githubusercontent.com/Skr0ut/Portfolio-1/main/Data.csv?token=AWRQD5K6OVZNAE5XWO6EKBTBUD5NI')

# Removal of Trial Blocks
    # Note: originally 13 participants; 1 did only a trial block so their data is excluded.
df = df[df.phase != 'practice']
print(df['phase'].unique())

## Outlier Replacing
# 1. Calculating mean RT's per subject for each flanker condition for non-outlier trials
    # Note: Outliers determined by RT's >200ms or <1000ms
df['rt_mean'] = df[(df['rt'].between(350,1000, inclusive=False))].groupby(['subj', 'flanker'])['rt'].transform(np.mean)

# 2. Replacing rows with RT's >200 & <1000 ms to have mean subject RT for each flanker condition
df['rt_mean'] = df.groupby(['subj', 'flanker'])['rt_mean'].transform(lambda x: x.fillna(np.nanmean(x)))

# 3. Creating rt_clean to rt_mean for trials not between 200 and 1000 ms
df['rt_clean'] = np.where((~df['rt'].between(350,1000, inclusive=False)), df['rt_mean'], df['rt'])
    ## To check if Data cleaning worked
    #x = (np.where(~df['rt'].between(200,1000, inclusive=False)))
    #y = (np.where(df['rt'].between(200,1000, inclusive=False)))
    #print(df.iloc[x]#.describe())
    #print(df.iloc[y]#.describe())



## Graphing
    # RT distribution for each flanker condition (Histogram)
#sns.displot(data=df, bins=15, x='rt_clean', hue='bias', col='flanker', alpha = .4, kind='hist', palette='gray')

    # Bias and RTs for each flanker condition (Box)
#sns.catplot(data=df, x='bias', y='rt_clean', col='flanker', kind='box', palette='gray')

    # Error Rates for each flanker condition across both biases (Bar)
#sns.catplot(data=df, x='flanker', y='err', col='bias', kind='bar', palette='gray')

sns.relplot(data=df, x='rt_clean', y='err', col='bias', hue='flanker', kind='line', palette='gray')

plt.show()

#plt.savefig('RT-distribution.tiff', dpi=300)