import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics
import math
with open("data_x.csv")as f:
    lst=list(csv.reader(f))
with open("data_time.csv")as f:
    lst1=list(csv.reader(f))
with open("data_ud.csv")as f:
    lst3=list(csv.reader(f))
size=int((len(lst))/5)
Fx=[[0]*size for i in range(5)]
lst2=[0]*size
print(size)
for i in range(0,size):
    lst2[i]=float(lst1[i][0])
    Fx[0][i]=int(lst[i*5][0])-int(lst[0][0])
    Fx[1][i]=int(lst[i*5][1])-int(lst[0][1])
    Fx[2][i]=int(lst[i*5][2])-int(lst[0][2])
    Fx[3][i]=int(lst[i*5][3])-int(lst[0][3])
    Fx[4][i]=int(lst[i*5][4])-int(lst[0][4])
    Fx[0][i]=0.3424*Fx[0][i]
    Fx[1][i]=0.3416*Fx[1][i]
    Fx[2][i]=0.3354*Fx[2][i]
    Fx[3][i]=0.3964*Fx[3][i]
    Fx[4][i]=0.2664*Fx[4][i]
with open('data_xxx.csv','w',newline="")as f:
    writer = csv.writer(f)
    writer.writerows(Fx)
for i in range(size):
    if Fx[4][i]<-25 and Fx[4][i-1]>=-25:
        print(lst2[i])

#fig=plt.figure(figsize=(18,4))
fig=plt.figure(figsize=(18,6))
#plt.title("Fx")
plt.plot(lst2,Fx[0],color="r",label="Fx1")
plt.plot(lst2,Fx[1],color="b",label="Fx2")
plt.plot(lst2,Fx[2],color="y",label="Fx3")
plt.plot(lst2,Fx[3],color="g",label="Fx4")
plt.plot(lst2,Fx[4],color="m",label="Fx5")
plt.xlim(0,14.5)
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0,fontsize=18)
plt.ylim(-20,20)
plt.xlabel("time[s]",fontsize=18)
plt.ylabel("Fx[N]",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.subplots_adjust(right=0.85)
fig.savefig("Fx.svg")
plt.show()
#print(str(lst3[2][0]))

#jd=[[51,68],[77,93],[105,122],[133,153],[165,181],[192,211],[225,240],[251,271],[283,303]]
jd=[[41,60],[75,93],[106,124],[134,154],[165,178],[187,206],[218,238],[249,263],[277,295]]
per=[0]*8
for i in range(8):
    per[i]=lst2[jd[i+1][0]]-lst2[jd[i][0]]
print(statistics.mean(per))
print(statistics.stdev(per))
na=int(len(jd))
Sx=[[0]*9 for i in range(5)]
k=0
for i in range(na):
    for j in range(jd[i][0],jd[i][1]):
        Sx[0][k]+=Fx[0][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[1][k]+=Fx[1][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[2][k]+=Fx[2][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[3][k]+=Fx[3][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[4][k]+=Fx[4][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
    k+=1
print(Sx)
means=[0]*5
stds=[0]*5
for i in range(5):
    means[i]=statistics.mean(Sx[i])
    stds[i]=statistics.stdev(Sx[i])
print(means)
print(stds)
with open('impulse_x.csv','w',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Sx)
            