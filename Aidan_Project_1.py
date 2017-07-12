# Using pandas

print("Pandas Calculations")
print("")
# setup
import pandas as pd
df = pd.read_csv('Sample_Dataset.csv')
# mean
print("Total:",df['Total'].mean(),"Native:",df['Native'].mean())
# median
print(df['Total'].median(),df['Native'].median())
# mode
print(df['Total'].mode(),df['Native'].mode())
# range
print([df['Total'].max(),df['Total'].min()],[df['Native'].max(),df['Native'].min()])


# Using NumPy

# setup
import numpy as np
df = np.genfromtxt('Sample_Dataset.csv', delimiter = ',', usecols = (2,3))
df = np.delete(df, (0), axis=0)
# mean
print(df.mean(axis=0))
# medium
print(np.median(df, axis=0))
# mode
from scipy import stats
print(stats.mode(df,axis=0))
# range
print(np.amax(df, axis=0),np.amin(df,axis=0))


# In Basic Python

# setup
import pyexcel as p
sheet = p.get_sheet(file_name="Sample_Dataset.csv")
del sheet.row[0]
total = sheet.column[2]
total = list(total)
native = sheet.column[3]
native = list(native)
# mean
total_mean = float(sum(total))/float(len(total)) #mean total
native_mean = float(sum(native))/float(len(native)) #mean native
print(total_mean,native_mean)
# median
total.sort()
native.sort()
thalf = len(total)/2 
thalf = int(thalf)
if thalf % 2 == 0:
 total_med = total[thalf] + total[thalf-1]
 total_med = total_med/2
else:
 total_med = total[thalf] 
print(total_med) # median total
if thalf % 2 == 0:
 native_med = native[thalf] + native[thalf-1]
 native_med = native_med/2
else:
 native_med = native[thalf]
print(native_med) # median native
# range
total.sort()
native.sort()
r = len(total)
r = r-1 
r = int(r)
print(total[r],total[0]) # total range
print(native[r],native[0]) # native range
# mode total
store_tot = []
tot_mode = []
for item in total:
 if store_tot == []:
  store_tot = total
 else:
  total = store_tot
 store1 = item 
 total.remove(item)
 for number in total:
  if store1 == number:
   tot_mode.append(number) # total mode
print(tot_mode)
# mode native
store_nat = []
nat_mode = []
for item in native:
 if store_nat == []:
  store_nat = native
 else:
  native = store_nat
 store2 = item 
 native.remove(item)
 for number in native:
  if store2 == number:
   nat_mode.append(number) # native mode
print(nat_mode)