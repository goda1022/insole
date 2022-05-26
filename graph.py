import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np

with open("stress2.csv")as f:
    lst=list(csv.reader(f))

size=int(len(lst)/5)
Fz1=[0]*size
Fz2=[0]*size
Fz3=[0]*size
#Fz4=[0]*size
#Fz5=[0]*size
Fz=[0]*5

for i in range(size):
    Fz1[i]=float(lst[i*5][0])-float(lst[0][0])
    Fz2[i]=float(lst[i*5][1])-float(lst[0][1])
    Fz3[i]=float(lst[i*5][2])-float(lst[0][2])
    #Fz4[i]=float(lst[i*5][3])-float(lst[0][3])
    #Fz5[i]=float(lst[i*5][4])-float(lst[0][4])
fig=plt.figure(figsize=(15,4))
#plt.title("Fz")
plt.plot(Fz1,color="r",label="Fz1")
plt.plot(Fz2,color="b",label="Fz2")
plt.plot(Fz3,color="y",label="Fz3")
#plt.plot(Fz4,color="g",label="Fz4")
#plt.plot(Fz5,color="m",label="Fz5")
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0,fontsize=18)
plt.ylim(-10,100)
plt.xlabel("データ数",fontname="MS Gothic",fontsize=18)
plt.ylabel("インソールセンサの出力",fontname="MS Gothic",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.subplots_adjust(right=0.85)
fig.savefig("graphr.png")
plt.show()

