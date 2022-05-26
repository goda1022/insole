import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics
with open("data_y.csv")as f:
    lst=list(csv.reader(f))
with open("data_time.csv")as f:
    lst1=list(csv.reader(f))
size=int((len(lst))/5)
lst2=[0]*size
Fy=[[0]*size for i in range(5)]
for i in range(0,size):
    lst2[i]=float(lst1[i][0])
    Fy[0][i]=int(lst[i*5][0])-int(lst[0][0])
    Fy[1][i]=int(lst[i*5][1])-int(lst[0][1])
    Fy[2][i]=int(lst[i*5][2])-int(lst[0][2])
    Fy[3][i]=int(lst[i*5][3])-int(lst[0][3])
    Fy[4][i]=int(lst[i*5][4])-int(lst[0][4])
    Fy[0][i]=0.3523*Fy[0][i]
    Fy[1][i]=0.3344*Fy[1][i]
    Fy[2][i]=0.3707*Fy[2][i]
    Fy[3][i]=0.3780*Fy[3][i]
    Fy[4][i]=0.2875*Fy[4][i]
with open('data_yyy.csv','w',newline="")as f:
    writer = csv.writer(f)
    writer.writerows(Fy)
fig=plt.figure(figsize=(18,4))
#fig=plt.figure(figsize=(18,6))
#plt.title("Fy")
plt.plot(lst2,Fy[0],color="r",label="Fy1")
plt.plot(lst2,Fy[1],color="b",label="Fy2")
plt.plot(lst2,Fy[2],color="y",label="Fy3")
plt.plot(lst2,Fy[3],color="g",label="Fy4")
plt.plot(lst2,Fy[4],color="m",label="Fy5")
plt.xlim(0,14.5)
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0,fontsize=18)
plt.ylim(-20,20)
#plt.xlabel("time[s]",fontsize=18)
plt.ylabel("Fy[N]",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.subplots_adjust(right=0.85)
fig.savefig("Fy.svg")
plt.show()

#jd=[[51,68],[77,93],[105,122],[133,153],[165,181],[192,211],[225,240],[251,271],[283,303]]
jd=[[41,60],[75,93],[106,124],[134,154],[165,178],[187,206],[218,238],[249,263],[277,295]]
na=int(len(jd))
Sx=[[0]*9 for i in range(5)]
k=0
for i in range(na):
    for j in range(jd[i][0],jd[i][1]):
        Sx[0][k]+=Fy[0][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[1][k]+=Fy[1][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[2][k]+=Fy[2][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[3][k]+=Fy[3][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[4][k]+=Fy[4][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
    k+=1
print(Sx)
means=[0]*5
stds=[0]*5
for i in range(5):
    means[i]=statistics.mean(Sx[i])
    stds[i]=statistics.stdev(Sx[i])
print(means)
print(stds)
with open('impulse_y.csv','w',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Sx)    
