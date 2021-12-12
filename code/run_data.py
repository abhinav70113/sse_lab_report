import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import mesa_reader

mpl.rcParams.update(mpl.rcParamsDefault)
#h = mesa_reader.MesaData('/Users/abhinavtyagi/Desktop/scp_data/LOGS/history.data')
df_data = pd.read_csv('/df_1Msun_history.csv')
df = df_data[df_data['star_age']<20e15]
#df_data['star_age'] = df_data['star_age'].astype(int)

plt.figure()
Teff = df['log_Teff']
L = df['log_L']
plt.xlim(max(Teff),min(Teff))
plt.scatter(Teff, L , c = df['star_age'])
plt.xlabel(r'$\mathrm{log (T_{eff}/[K]})$')
plt.ylabel(r'$\mathrm{log (L/L_{\odot})}$')
plt.colorbar(label = 'Age of the star [yrs]')
plt.title('HR Diagram of 1 Solar Mass star')
plt.scatter(3.76,0, marker='*', color = 'red', s = 150, label='sun')
plt.legend()
plt.savefig('HRplot.pdf')
plt.show()

df = df_data[df_data['star_age']<12.53e9]
plt.figure()
Teff = df['log_Teff']
L = df['log_L']
plt.xlim(max(Teff),min(Teff))
plt.scatter(Teff, L , c = df['star_age'])
plt.xlabel(r'$\mathrm{log (T_{eff}/[K]})$')
plt.ylabel(r'$\mathrm{log (L/L_{\odot})}$')
plt.colorbar(label = 'Age of the star [yrs]')
plt.title('HRD of 1 Solar-mass star below 12.53e9 years')
plt.scatter(3.76,0, marker='*', color = 'red', s = 150, label='sun')
plt.legend()
plt.savefig('HRplot1.pdf')