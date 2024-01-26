from matplotlib import pyplot as plt
from numpy import random as rnd
prove = [0,15,30,45,100,-75]
asse = ["A","B","C","D","E", "F"]
ax = rnd.randint(0,100,20)
plt.plot(prove, asse ,"y", linewidth = 4, marker = "o", markersize = 12, linestyle = "--")
plt.xlabel("Asse dei numeri" , color= "#9999ff")
plt.ylabel("Asse delle lettere" , color=(.7,.3,.1))
plt.grid(True)
plt.legend("Legenda", loc= 'best')

#plt.subplot(1,2,1)
#plt.plot(prove, asse, "b^")
plt.pie(ax)
plt.hist(prove)
#plt.savefig("Grafico", dpi = 100)
plt.show()


#import seaborn as sns
#import matplotlib.pyplot as plt
#anscombe = sns.load_dataset("anscombe")
#print(anscombe.sample(10))
#datasetI = anscombe[anscombe.dataset == "I"]
#sns.lmplot(data = datasetI, x='x', y='y')
#plt.show()

import pandas as pd
from matplotlib import pyplot as plt
from numpy import random as rnd
file_name = "./stockdata.csv"
borse = pd.read_csv(file_name, sep = ",")
print(borse)
print(borse.describe())
print(borse.count())
MSFT = borse.iloc[:, 0]
Andamento = pd.to_datetime(borse.iloc[:, -1])

plt.plot(MSFT, Andamento, "b",linewidth = 2, marker = "o", markersize = 3, linestyle = "--")
plt.title('Microsoft in Borsa')
plt.xlabel('Prezzi', color= "#9999ff")
plt.ylabel('Date', color= (.3,.5,.2))
plt.legend("Legenda", loc= 'best')
plt.grid(True)
plt.show()


import pandas as pd
from matplotlib import pyplot as plt
from numpy import random as rnd
file_name = "./stockdata.csv"
borse = pd.read_csv(file_name, sep = ",")
print(borse)
print(borse.describe())
print(borse.count())

prime_5_righe_MSFT = borse.iloc[5:,0]
prime_5_righe_Andamento = pd.to_datetime(borse.iloc[5:, -1])

plt.plot(prime_5_righe_MSFT, prime_5_righe_Andamento, "g",linewidth = 3, marker = "x", markersize = 2, linestyle = ":")
plt.title('Microsoft in Borsa, Prime 5 Righe Dataset')
plt.xlabel('Prezzi', color = "#9999ff")
plt.ylabel('Date', color = (.2,.6,.2))
plt.legend("Legenda", loc = 'center right')
plt.grid(True)
plt.show() 


import pandas as pd
from matplotlib import pyplot as plt
from numpy import random as rnd
file_name = "./stockdata.csv"
borse = pd.read_csv(file_name, sep = ",")
print(borse)
print(borse.describe())
print(borse.count())

ultime_5_righe_MSFT = borse.iloc[-5:,0]
ultime_5_righe_Andamento = pd.to_datetime(borse.iloc[-5:, -1])

plt.plot(ultime_5_righe_MSFT, ultime_5_righe_Andamento, "g",linewidth = 3, marker = "x", markersize = 2, linestyle = ":")
plt.title('Microsoft in Borsa, Ultime 5 Righe Dataset')
plt.xlabel('Prezzi', color = "#9999ff")
plt.ylabel('Date', color = (.2,.6,.2))
plt.legend("Legenda", loc = 'center right')
plt.grid(True)
plt.show()      



import pandas as pd
from matplotlib import pyplot as plt
from numpy import random as rnd
file_name = "./stockdata.csv"
borse = pd.read_csv(file_name, sep = ",")
print(borse.count())

AAPL = borse.iloc[:, 4]
Andamento_Apple = pd.to_datetime(borse.iloc[:, -1])

plt.plot(Andamento_Apple, AAPL, "r",linewidth = 2, marker = "o", markersize = 4, linestyle = ":", markerfacecolor = "k")
plt.title('Azioni APPLE')
plt.xlabel('Date', color = "#9999ff")
plt.ylabel('Valore', color = (.3,.3,.4))
plt.legend("Legenda", loc = 'center right')
plt.show()   



import pandas as pd
from matplotlib import pyplot as plt
from numpy import random as rnd

file_name = "./stockdata.csv"
borse = pd.read_csv(file_name, sep = ",")
borse.plot(x = borse.columns[-1], y = borse.columns[:-1] , linewidth = 2.5, marker ='o', linestyle='--' )

plt.title('Azioni')
plt.xlabel('Date', color="#9999ff")  
plt.ylabel('Prezzi', color=(.4, .3, .3)) 
plt.legend(borse.columns[:-1], loc= 'lower left')
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from numpy import random as rnd
file_name = "./election.csv"
elezioni = pd.read_csv(file_name)

candidati = ['Coderre', 'Bergeron', 'Joly']
totali = elezioni[candidati].sum()

totali.plot(kind ='bar', linewidth = 3)

plt.title('Voti Totali Candidati')
plt.xlabel('Candidati')
plt.ylabel('Voti Totali')
plt.show()




import pandas as pd
from matplotlib import pyplot as plt
from numpy import random as rnd
file_name = "./election.csv"
elezioni = pd.read_csv(file_name)
print(elezioni.describe())
print(elezioni.count())

grouped_data_uno = elezioni.groupby(elezioni.columns[-1])['Coderre'].sum()
grouped_data_due = elezioni.groupby(elezioni.columns[-1])['Bergeron'].sum()
grouped_data_tre = elezioni.groupby(elezioni.columns[-1])['Joly'].sum()



grouped_data_uno.plot(kind='bar', label='Coderre', color='blue')
grouped_data_due.plot(kind='bar', label='Bergeron', color='green')
grouped_data_tre.plot(kind='bar', label='Joly', color='red')
plt.title('Voti totali dei tre candidati')
plt.xlabel('Distretto', color="#9999ff")
plt.ylabel('Voti', color=(.3, .5, .2))
plt.legend(["Coderre"], loc='best')
plt.show()





import pandas as pd
from matplotlib import pyplot as plt

file_name = "./election.csv"
elezioni = pd.read_csv(file_name)


primi_quattro_distretti = elezioni['district_id'].head(4)

p_quattro = elezioni[elezioni['district_id'].isin(primi_quattro_distretti)]


candidato_uno = p_quattro.groupby(elezioni.columns[-1])['Coderre'].sum()
candidato_due = p_quattro.groupby(elezioni.columns[-1])['Bergeron'].sum()
candidato_tre = p_quattro.groupby(elezioni.columns[-1])['Joly'].sum()


candidato_uno.plot(label='Coderre', color='blue',linewidth = 2, linestyle = ":")
candidato_due.plot(label='Bergeron', color='green',linewidth = 2,linestyle = "--" )
candidato_tre.plot(label='Joly', color='red', linewidth = 3,linestyle = "-")

plt.title('Primi 4 distretti')
plt.xlabel('Distretti', color="#9999ff")
plt.ylabel('Voti', color=(.3, .5, .2))
plt.legend(loc='upper center')
plt.show()





import pandas as pd
from matplotlib import pyplot as plt

file_name = "./election.csv"
elezioni = pd.read_csv(file_name)

primi_quattro_distretti = elezioni['district_id'].head(4)

p_quattro = elezioni[elezioni['district_id'].isin(primi_quattro_distretti)]


candidato_uno = p_quattro.groupby(elezioni.columns[-1])['Coderre'].sum()
candidato_due = p_quattro.groupby(elezioni.columns[-1])['Bergeron'].sum()
candidato_tre = p_quattro.groupby(elezioni.columns[-1])['Joly'].sum()


fig, axes = plt.subplots(1, 3)
axes[0].pie(candidato_uno, labels=candidato_uno.index)
axes[0].set_title('Coderre')
axes[1].pie(candidato_due, labels=candidato_due.index)
axes[1].set_title('Bergeron')
axes[2].pie(candidato_tre, labels=candidato_tre.index)
axes[2].set_title('Joly')
plt.savefig('grafici Voti.png', dpi=300)
plt.suptitle("Ecco il Totale dei Voti")
plt.show()



import seaborn as sns 
titanic = sns.load_dataset('titanic')