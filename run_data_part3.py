import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import mesa_reader

mpl.rcParams.update(mpl.rcParamsDefault)
#h = mesa_reader.MesaData('/Users/abhinavtyagi/Desktop/scp_data/LOGS/history.data')
df_data = pd.read_csv('/df_1Msun_history.csv')
df = df_data[df_data['star_age']<20e15]

plt.figure()
M_no = df['model_number']
T_st = df['time_step']
#plt.xlim(max(Teff),min(Teff))
plt.scatter(M_no, T_st, c = df['star_age'], s=0.5)
plt.yscale('log')
plt.xlabel('Model number')
plt.ylabel(r'Log (Time step/[yrs])')
plt.title('Model number v/s time_step histogram')
plt.colorbar(label = 'Age of the star [yrs]')
plt.scatter(620,400000000, marker='*', color = 'red', s = 150, label='sun')

plt.legend()
#plt.savefig('HRplot.pdf')
plt.show()

