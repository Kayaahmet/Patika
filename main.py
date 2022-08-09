import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv("C:\covid_19_clean_complete.csv")

#sns.heatmap(data.isnull())
#plt.show()
# null verileri grafik ortamında görmeyi amaçladım.

#print(data.groupby('Country/Region')['Confirmed','Recovered','Deaths'].sum())
#ölüm iyileşen ve yakalanan hasta verisini grupladım.
data = data[~(data.Confirmed < 1000)] #1000 den küçük verileri sildim.


print(data.groupby('Country/Region').Confirmed.sum().sort_values(ascending = True).head(20)) # En düşük değerler
print(data.groupby('Country/Region').Confirmed.sum().sort_values(ascending = False).head(20)) # En yüksek değerler