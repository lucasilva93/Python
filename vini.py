import numpy as np
import pandas as pd
file_name = "./wine.csv"
vini = pd.read_csv(file_name,sep ="," ,encoding="iso-8859-15",header = 0)
print(vini)
print(vini.describe())
print(vini.count())

mediaV = vini.mean(axis= 0, numeric_only = True)
medianaV = vini.median(axis = 0, numeric_only= True)
modaV = vini.mode(axis = 0, numeric_only = True)
quartiliV = vini.quantile([0.25, 0.50, 0.75], axis = 0, numeric_only= True) 


print(mediaV)
print(medianaV)
print(modaV)
print(quartiliV)
