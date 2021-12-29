read_csv_address = '/Users/abhinavtyagi/PycharmProjects/pythonProject/035Msun/df_035Msun_history.csv'
save_fig_address = '/Users/abhinavtyagi/PycharmProjects/pythonProject/035Msun/HRplot035.pdf'

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update(mpl.rcParamsDefault)
df_data = pd.read_csv(read_csv_address)

df = df_data[(df_data['star_age']< 12e5) & (df_data['star_age'] > 0)]

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
plt.show()
plt.savefig(save_fig_address)
