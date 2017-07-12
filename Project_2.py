print("Data from Census Bureau")
print("")
import pandas as pd
from numpy import nan
from numpy import nanmean
df = pd.read_json("https://api.census.gov/data/2015/acs1/subject?get=NAME,S0501_C01_001E,S0501_C02_001E&for=state:*&key=your_key_here")
df = df.drop(df.index[0])
df.fillna(value=nan, inplace=True)
total = df.ix[:,1]
native = df.ix[:,2]
# mean
total = pd.to_numeric(total)
native = pd.to_numeric(native)
print("Mean")
print("Total: ", nanmean(total), " Native: ", nanmean(native))
print("")
# median
print("Median")
from numpy import nanmedian
print('Total: ', nanmedian(total), 'Native: ', nanmedian(native))
print('')
# mode
print("Mode")
print(total.mode(),native.mode())
print("")
# range
print("Range")
print("Total: ", total.max()- total.min(), "Native: ", native.max() - native.min())