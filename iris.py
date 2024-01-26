import numpy as np
import pandas as pd
file_name = "./iris.names.csv"
iris = pd.read_csv(file_name,sep ="," ,header = 0,  names =["Caratteristica", "Minimo", "Massimo", "Media", "SD", "Correlazione"])


print(iris)
print(iris.describe())
print(iris.count())

import numpy as np
import pandas as pd
file_name_1 = "./iris.data.csv"
iris_data= pd.read_csv(file_name_1, sep = ",", header = None, names = ["Massimo", "Minimo", "Media", "SD", "Pianta"])
print(iris_data.shape)
print(iris_data)
print(iris_data.head(5))
print(iris_data.tail(10))
print(iris_data.describe())
print(iris_data.count())
mediaid = iris_data.mean(axis= 0, numeric_only = True)
print(mediaid)
pd.DataFrame(iris_data)