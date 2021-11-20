import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#import base64
#from scipy.stats import ttest_ind

df = pd.read_csv('https://raw.githubusercontent.com/Skr0ut/Portfolio-1/main/Cleaned_Data.csv?token=AWRQD5PWCLJ7FB26ITHTDEDBUKBLA')

## Attentional Network Subtractions
# Executive Control (Incongruent - Congruent Trials)
dfEC = df[(df['flanker'] != 'None') & (df['subj']) & (df['rt_clean'])]
#dfEC['EC_score'] = dfEC.groupby(['subj']).transform(dfEC['incongruent'] - dfEC['incongruent'])

#print(dfEC.groupby(['subj', 'flanker'])['rt_clean'].describe())

# Alerting (Tone present - tone absent (for non visually cued trials only))


# Orienting (Cue present - cue absent (for non tone cued trials only))
