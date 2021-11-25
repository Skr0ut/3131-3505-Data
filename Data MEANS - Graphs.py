import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

dfM = pd.read_csv('https://raw.githubusercontent.com/Skr0ut/3131-3505-Data/main/Data/3131%20Data%20MEANS.csv')
print(dfM.sample(15))


sns.relplot(data=dfM, x='rt', y='acc', col='flanker', hue='bias', kind='line', palette='Paired')

plt.show()