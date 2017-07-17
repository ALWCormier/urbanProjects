#setup
print("Population and Gender-split by State")
print("")
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_json("https://api.census.gov/data/2015/acs1/subject?get=NAME,S0101_C01_001E,S0101_C02_001E,S0501_C02_001E&for=state:*&key=94c7b892e6cf07a1404cbb9dd12a60d8391cda46")

#1st dataset
#isolating single data columns
df = df.drop(df.index[0])
men = df.iloc[:,2]
men = pd.to_numeric(men)
total_men = men.sum()
total = df.iloc[:,1]
total_num = pd.to_numeric(total)
total_total = total_num.sum()
total_women = total_total - total_men

#formatting for 1st graph
footer = ['']
men_women_graph = pd.DataFrame({"Men": total_men, 'Women': total_women}, index=footer)
df1 = men_women_graph.plot(kind='bar', title="Number of Women vs. Men in the United States")
df1.set_xlabel(" ")
df1.set_ylabel("Number (by hundred million)")
plt.show()
print(men_women_graph)
print('')
print("Interestingly there are slightly more women than men in the United States, however it is still very close to the 50-50 split one might expect it to be.")
print("")

#2nd dataset
#column select
state = df.iloc[:,0]
total_lst = list(total)
state_lst = list(state)
total_lst = pd.to_numeric(total_lst)
men_lst = list(men)

#dividng for percent calculations
per_lst = [c/t for c,t in zip(men_lst, total_lst)]
low_men = min(per_lst)
high_men = max(per_lst)
state_dict = dict(zip(per_lst, state_lst))
lms = state_dict.get(low_men)
hms = state_dict.get(high_men)
high_men = high_men * 100
low_men = low_men * 100

#formatting for 2nd graph
trg_st = [""]
new_dict = {hms: high_men, lms:low_men}
df2 = pd.DataFrame(new_dict, index=trg_st)
graph_2 = df2.plot(kind = "bar", title = "States With The Most and Least Men by Percent")
graph_2.set_xlabel("Most Men          Least Men")
graph_2.set_ylabel("Percent")
plt.show()
print(hms,":", high_men,"%    ",lms,":",low_men,"%")
print('')
print("By takingt the totals of men and women and getting percent breakdown of the gender split by state we find that like the total population the split is fairly close to 50-50. Even in the states with the largest difference it is no more than 5%. Interestingly the state with the most men has less of a difference than the state with the most women, probably attributable to the fact that there are several million more women overall in the United States.")
print("")

#3rd dataset
#column select
native = df.iloc[:,3]
native = pd.to_numeric(native)
total_native = native.sum()

#3rd graph setup
total_foreign = total_total - total_native
native_foreign_graph = pd.DataFrame({"Native": total_native, 'Foreign': total_foreign}, index=footer)
df3 = native_foreign_graph.plot(kind='bar',title="Number of Native Born vs. Foreign People in the United States")
df3.set_xlabel(" ")
df3.set_ylabel("Number (by hundred million)")
plt.show()
print(native_foreign_graph)
print("")
print("There are over five times more native born residents in the United States than foreign born, a statistic that one would naturally expect of any country. Even the foreign born residents contribute to the growth of the native populace by having children, and immigration could not feasibly spike to a level great enough to compete with the cummulative growth of the native population inside reasonable circumstances, meaning this natural discrepancy will persist.")



