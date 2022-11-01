import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import csv
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#1

heart = pd.read_csv('Coding Python Ms Nurul\Heart.csv', index_col = 0) #2 #this is for number 4 which remove the unnamed
# print (heart)#3

# print(heart.head(5)) #5
# print(heart.tail(5)) #6

# print(heart.count())
# print(heart.max())
# print(heart.min())
# print(heart.mean())
# print(heart.std())
# print(heart.median())
# print(heart.describe()) #7

# print(heart.isna().sum()) #8

# heart = heart.dropna()#9
# print(heart.count())

# sns.heatmap(heart.corr()) #10

# fig, ax = plt.subplots(figsize=(10,6))
# r = sns.heatmap(heart.corr(), center=0, cmap='BrBG', annot=True)
# r.set_title("Heart")

# print(heart["Age"]) #11

#12
old = []
middle = []
young = []

for i in heart["Age"] :
    if int(heart["Age"][i]) < 40 :
        young.append(heart["Age"][i])
    elif int(heart["Age"][i]) > 55 :
        old.append(heart["Age"][i])
    else:
        middle.append(heart["Age"][i])

# print(old)
# print(middle)
# print(young)
#12

#13
# bar_easy = ["Young","Middle", "Old"]
# bar_hard = [len(young),len(middle),len(old)]

# x_pos = np.arange(len(bar_hard))
 
# # Create bars
# plt.bar(x_pos, bar_easy)
 
# # Create names on the x-axis
# plt.xticks(x_pos, bar_hard)
 
# # Show graphic
# plt.show()
#13

#14
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(young, middle, old,
#            linewidths=1, alpha=.7,
#            edgecolor='k',
#            s = 200,
#            c=old)
# plt.show()
#14

#15
# y = [len(young),len(middle),len(old)]

# plt.pie(y)
# plt.show() 
#15

for i in heart["Age"] :
    print(int(heart["Age"][i])) #16

print(heart.corr()) #17

scaler = StandardScaler()
print(scaler.transform(heart)) #18