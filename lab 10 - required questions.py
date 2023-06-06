
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('/Users/nihaa/Downloads/movies.csv', 
   header = None, 
   names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

sh = sh_raw[np.isfinite(
          sh_raw.OpeningWeekendBoxOffice)]
print(sh.head(5))

''' Output
    Year            Title  ... EstdOpeningAttendance  USPopThatYear
1  1978.0         Superman  ...           3190317.521    222584545.0
2  1980.0      Superman II  ...           5241830.112    227224681.0
4  1983.0     Superman III  ...           4238843.492    233791994.0
5  1984.0        Supergirl  ...           1707812.202    235824902.0
6  1986.0  Howard the Duck  ...           1366613.477    240132887.0

[5 rows x 10 columns]
'''
 

# Normalize and scatterplot the scores
imdb_normalized = sh.IMDB / 10         
sh.insert(10,'IMDBNormalized',imdb_normalized)
rt_normalized = sh.RT/100        
sh.insert(11, 'RTNormalized', rt_normalized)
sh.plot.scatter(x ='RTNormalized', y ='IMDBNormalized')
plt.show()

print(sh[['RTNormalized','IMDBNormalized']].corr())
print(sh[['RTNormalized','IMDBNormalized']].describe())


''' OUTPUT

                RTNormalized  IMDBNormalized
RTNormalized         1.00000         0.88836
IMDBNormalized       0.88836         1.00000
       RTNormalized  IMDBNormalized
count     46.000000       46.000000
mean       0.539783        0.630000
std        0.302129        0.152898
min        0.080000        0.270000
25%        0.260000        0.540000
50%        0.605000        0.665000
75%        0.812500        0.740000
max        0.950000        0.910000
'''
#print the Series rows for the 'DC' comic movies from the sh DataFrame. There should be 18 rows.
print(sh[sh['Comic'] =='DC'])
#print just 2 columns - the Year and the Title columns of only 'DC' comic movies from the sh DataFrame.
print(sh[sh['Comic'] == 'DC'][['Year', 'Title']])
#print just 2 columns - the Year and Title columns of only 'Marvel' movies from the sh DataFrame.
print(sh[sh['Comic'] == 'Marvel'][['Year', 'Title']])
#plot a scatterplot  for the AvgTicketPriceThatYear on the y-axis and with Year on the x axis.
sh.plot.scatter(x ='Year', y ='AvgTicketPriceThatYear')
plt.show()
#print the correlation for the Year versus the AvgTicketPriceThatYear.
print(sh[['Year','AvgTicketPriceThatYear']].corr())

#print the summary statistics for OpeningWeekendBoxOffice.
print(sh['OpeningWeekendBoxOffice'].describe())
