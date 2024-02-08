import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

file_dir = "./dataset_climatico.csv"

table = pd.read_csv(file_dir)
dati_puliti = table.dropna().drop_duplicates()
print(dati_puliti.describe().round(2))
#print(dati_puliti.tail(10)) #da riga 990 alla 999 

#temperatura_media_per_stazione = dati_puliti.groupby('stazione_meteorologica')['temperatura_media'].mean()
# temperatura media dei primi 3 valori: temperatura_3 = dati_puliti['temperatura_media'].head(3).mean()

#dati_puliti['zscore'] = (dati_puliti['temperatura_media'] - dati_puliti['temperatura_media'].mean()) / dati_puliti['temperatura_media'].std(ddof=0)


deviazione_std_temperatura_media = np.std(dati_puliti["temperatura_media"])
print("La deviazione standard della temperatura è: ", deviazione_std_temperatura_media)
media_temperatura = np.mean(dati_puliti["temperatura_media"])
print("La temperatura media è : ", media_temperatura)
deviazione_std_umidita = np.std(dati_puliti["umidita"])
print("La deviazione standard dell'umidità è: ", deviazione_std_umidita)
media_umidita = np.mean(dati_puliti["umidita"])
print("L'umidità media è: ", media_umidita)
deviazione_std_precipitazioni = np.std(dati_puliti["precipitazioni"])
print("La deviazione standard delle precipitazioni è: : ", deviazione_std_precipitazioni)
media_precipitazioni = np.mean(dati_puliti["precipitazioni"])
print("Le precipitazioni medie sono: ", media_precipitazioni)
deviazione_std_velocita_vento = np.std(dati_puliti["velocita_vento"])
print("La deviazione standard della velocità del vento è: ", deviazione_std_velocita_vento)
media_velocita_vento = np.mean(dati_puliti["velocita_vento"])
print("La velocità media del vento è: ", media_velocita_vento)

dati_puliti['temperatura_media_z'] = stats.zscore(dati_puliti['temperatura_media'])
dati_puliti['precipitazioni_z'] = stats.zscore(dati_puliti['precipitazioni'])
dati_puliti['umidita_z'] = stats.zscore(dati_puliti['umidita'])
dati_puliti['velocita_vento_z'] = stats.zscore(dati_puliti['velocita_vento'])
print(dati_puliti[['temperatura_media_z', 'precipitazioni_z', 'umidita_z', 'velocita_vento_z']])
statistiche = dati_puliti[['temperatura_media_z', 'precipitazioni_z', 'umidita_z', 'velocita_vento_z']].describe()
print(statistiche)

plt.figure(figsize=(15,10))
plt.subplot(2, 2, 1)
plt.hist(dati_puliti['temperatura_media_z'], bins=30, color='red', edgecolor='black', alpha=0.5)
plt.title('Temperature')
plt.subplot(2, 2, 2)
plt.hist(dati_puliti['precipitazioni_z'], bins=30, color='c', edgecolor='black', alpha=0.5)
plt.title('Precipitazioni')
plt.subplot(2, 2, 3)
plt.hist(dati_puliti['umidita_z'], bins=30, color='b', edgecolor='black', alpha=0.5)
plt.title('Umidità')
plt.subplot(2, 2, 4)
plt.hist(dati_puliti['velocita_vento_z'], bins=30, color='purple', edgecolor='black', alpha=0.5)
plt.title('Vento')
plt.show()

plt.figure(figsize = (10,10))
sns.boxplot(data = dati_puliti[['temperatura_media_z', 'precipitazioni_z', 'umidita_z', 'velocita_vento_z']])
plt.xlabel('Variabile')
plt.ylabel('Valore normalizzato Z-score')
plt.title('Box Plot delle variabili normalizzate')
plt.savefig('Box Plot delle variabili normalizzate.png')
plt.show()


plt.figure(figsize = (10,10))
colonne_numeriche = dati_puliti.select_dtypes(include='number').columns[0:4]
corr_matrix = dati_puliti[colonne_numeriche].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.1f', linewidths=.8)
plt.title('Matrice di Correlazione tra Variabili Meteorologiche')
plt.xticks(rotation = 55) 
plt.savefig('clima_normalizzato.png')
plt.show()
