import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np

with open("stress2.csv")as f:
    lst=list(csv.reader(f))

size=int(len(lst))
Fz1=[0]*size
Fz2=[0]*size
Fz3=[0]*size
Fz4=[0]*size
Fz5=[0]*size


for i in range(size):
    Fz1[i]=float(lst[i][0])-float(lst[0][0])
    Fz2[i]=float(lst[i][1])-float(lst[0][1])
    Fz3[i]=float(lst[i][2])-float(lst[0][2])
    #Fz4[i]=float(lst[i*5][3])-float(lst[0][3])
    #Fz5[i]=float(lst[i*5][4])-float(lst[0][4])
fig=plt.figure(figsize=(15,6))
#plt.title("Fz")
plt.plot(Fz1,color="r",label="Fx")
plt.plot(Fz2,color="b",label="Fy")
plt.plot(Fz3,color="y",label="Fz")
#plt.plot(Fz4,color="g",label="Fz4")
#plt.plot(Fz5,color="m",label="Fz5")
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0,fontsize=18)
plt.xlim(0,size)
plt.ylim(-10,60)
plt.xlabel("データ数[個]",fontname="MS Gothic",fontsize=18)
plt.ylabel("フォースセンサセンサの出力[N]",fontname="MS Gothic",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.subplots_adjust(right=0.85)
fig.savefig("graphr.png")
plt.show()

