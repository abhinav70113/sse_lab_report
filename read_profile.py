import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('/Users/abhinavtyagi/Desktop/scp_data/LOGS/profile91.data', 'r') as txt_file:
    data = txt_file.readlines()

columns = data[5].split()
df_data = pd.DataFrame(columns = columns)

for i in range(5,len(data)):
    words = data[i].split()
    df_data.loc[i-5] = words
df_data = df_data[1:]

df_data = df_data.astype(float)
#df_data['star_age'] = df_data['star_age'].astype(int)
df_data.to_csv('df_profile91.csv')

