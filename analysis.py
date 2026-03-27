import pandas as pd 
import matplotlib.pyplot as plt

folder_symmetric = 'naca0012_data.txt'
folder_hump = 'naca4412_data.txt'

columns = ['alpha','CL','CD','CDp','Cm','Top_Xtr','Bot_Xtr','Cpmin','Chinge','XCp']

df0012 = pd.read_csv(folder_symmetric, skiprows=11, sep=r'\s+', names=columns, usecols=range(10))
df4412 = pd.read_csv(folder_hump, skiprows=11, sep=r'\s+', names=columns, usecols=range(10))

plt.figure(figsize=(10, 6))

plt.plot(df0012['alpha'], df0012['CL'], 'b-o', label = 'NACA 0012(symmetric)', markersize=4)

plt.plot(df4412['alpha'], df4412['CL'], 'r-s', label = 'NACA 4412 (hump)', markersize = 4)

plt.title('Aviations Project : Foil Performance Comparing', fontsize=14)
plt.xlabel('Attack Angle(Alpha-degree)', fontsize=12)
plt.ylabel('Transport Coefficient (CL)', fontsize = 12)
plt.grid(True, linestyle='--', alpha = 0.7)
plt.axhline(0, color='black', linewidth = 1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()

plt.savefig('foil_analysis_result.png')
plt.show()

print("Graph is created and save as 'foil_analysis_result.png' ")
