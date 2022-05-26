import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics
with open("data_z.csv")as f:
    lst=list(csv.reader(f))
with open("data_time.csv")as f:
    lst1=list(csv.reader(f))
size=int(len(lst)/5)
Fz1=[0]*size
Fz2=[0]*size
Fz3=[0]*size
Fz4=[0]*size
Fz5=[0]*size
lst2=[0]*size
Fz=[[0]*size for i in range(5)]
jd=[[0]*2 for i in range(size)]
ud=[[0]*2 for i in range(size)]
tt=16
for i in range(size):
    #lst1[i]=float(lst1[i][0])
    lst2[i]=float(lst1[i][0])
    Fz[0][i]=int(lst[i*5][0])-int(lst[0][0])
    Fz[1][i]=int(lst[i*5][1])-int(lst[0][1])
    Fz[2][i]=int(lst[i*5][2])-int(lst[0][2])
    Fz[3][i]=int(lst[i*5][3])-int(lst[0][3])
    Fz[4][i]=int(lst[i*5][4])-int(lst[0][4])
    Fz[0][i]=Fz[0][i]*0.4824#Fz1[i]*0.0073-0.0737*Fz1[i]
    Fz[1][i]=Fz[1][i]*47.3/69
    Fz[2][i]=Fz[2][i]*40.3/73.9
    Fz[3][i]=Fz[3][i]*39.9/91.9
    Fz[4][i]=Fz[4][i]*45.9/89.1
    if Fz[0][i]>=tt or Fz[1][i]>=tt or Fz[2][i]>=tt or Fz[3][i]>=tt or Fz[4][i]>=tt:
        jd[i][0]=i
        jd[i][1]=1
    else:
        jd[i][0]=i
        jd[i][1]=0
with open('data_z_judge.csv','w',newline="")as f:
    writer = csv.writer(f)
    writer.writerows(jd) 
with open('data_zzz.csv','w',newline="")as f:
    writer = csv.writer(f)
    writer.writerows(Fz)
j=0
for i in range(1,size):
    ch=0
    if (jd[i][1]==1 and jd[i-1][1]==0):
        ud[j][0]=jd[i][0]
        j+=1
        ch=1
    if (jd[i][1]==0 and jd[i-1][1]==1):
        ud[j][0]=jd[i-1][0]
        j+=1
        ch=1
    # if ch==1:
    #     with open('ud.csv','a',newline="")as f:
    #         writer = csv.writer(f)
    #         writer.writerow(ud[j-1])
#fig=plt.figure(figsize=(18,4))
fig=plt.figure(figsize=(18,6))
#plt.rcParams['figure.subplot.bottom'] = 0.25
#plt.title("Fz")
plt.plot(lst2,Fz[0],color="r",label="Fz1")
plt.plot(lst2,Fz[1],color="b",label="Fz2")
plt.plot(lst2,Fz[2],color="y",label="Fz3")
plt.plot(lst2,Fz[3],color="g",label="Fz4")
plt.plot(lst2,Fz[4],color="m",label="Fz5")
#plt.axhline(y=10,xmin=0,color="black")
uud=[0]*j
for i in range(j):
     uud[i]=ud[i][0]
     plt.vlines(x=lst2[ud[i][0]],ymin=-30,ymax=100,color="black")
#     print(str(lst2[ud[i][0]])+','+str(ud[i][0]))
#plt.hlines(y=20,xmin=0,xmax=100,color="black")
with open('data_ud.csv','w',newline='')as f:
    writer = csv.writer(f)
    writer.writerow(uud)
print(uud)
plt.xlim(0,14.5)
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0,fontsize=18)
plt.ylim(-10,80)
plt.xlabel("time[s]", fontsize=18)
plt.ylabel("Fz[N]", fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.subplots_adjust(right=0.85)
fig.savefig("Fz_timeline.svg")
plt.show()
#jd=[[51,68],[77,93],[105,122],[133,153],[165,181],[192,211],[225,240],[251,271],[283,303]]
jd=[[41,60],[75,93],[106,124],[134,154],[165,178],[187,206],[218,238],[249,263],[277,295]]
per=[0]*8

na=int(len(jd))
Sx=[[0]*9 for i in range(5)]
k=0
for i in range(na):
    for j in range(jd[i][0],jd[i][1]):
        Sx[0][k]+=Fz[0][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[1][k]+=Fz[1][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[2][k]+=Fz[2][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[3][k]+=Fz[3][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
        Sx[4][k]+=Fz[4][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/((jd[i][1]-jd[i][0]))
    k+=1
print(Sx)
means=[0]*5
stds=[0]*5
for i in range(5):
    means[i]=statistics.mean(Sx[i])
    stds[i]=statistics.stdev(Sx[i])
print(means)
print(stds)
with open('impulse_z.csv','w',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Sx)
