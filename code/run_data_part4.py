import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import mesa_reader

mpl.rcParams.update(mpl.rcParamsDefault)
#h = mesa_reader.MesaData('/Users/abhinavtyagi/Desktop/scp_data/LOGS/history.data')
df_data = pd.read_csv('/Users/abhinavtyagi/PycharmProjects/pythonProject/CSVs/df_profile91.csv')
df = df_data
#df = df_data[df_data['star_age']<20e15]
df['radius_color'] = df['radius']*100000
df['radius_color'] = df['radius_color'].astype(int)


plt.figure()
Zone = df['zone']
x_frac = df['x_mass_fraction_H']
y_frac = df['y_mass_fraction_He']
z_frac = df['z_mass_fraction_metals']
#plt.xlim(max(Teff),min(Teff))
plt.scatter(Zone, x_frac, label='Hydrogen', c = df['radius_color'])
plt.scatter(Zone, y_frac, label='Helium', c = df['radius_color'])
plt.scatter(Zone, z_frac, label='Metals', c = df['radius_color'])
#plt.yscale('log')
plt.xlabel('Zone')
plt.ylabel(r'Composition')
plt.title(r'Composition of a $1M_\odot$ star')
plt.colorbar(label = 'radial coordinate * 100000')
#plt.scatter(620,400000000, marker='*', color = 'red', s = 150, label='sun')

plt.legend()
plt.savefig('/Users/abhinavtyagi/PycharmProjects/pythonProject/images/composition.png')
plt.show()

