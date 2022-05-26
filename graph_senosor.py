import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics
import math
with open("data_xxx.csv")as f:
    lstx=list(csv.reader(f))
with open("data_yyy.csv")as f:
    lsty=list(csv.reader(f))
with open("data_zzz.csv")as f:
    lstz=list(csv.reader(f))
with open("data_time.csv")as f:
    lstt=list(csv.reader(f))
with open("data_ud.csv")as f:
    lstu=list(csv.reader(f))
size=len(lstz[0])
sizet=(len(lstt))
print(size)
print(sizet)
size=min(size,sizet)
lstx0=[[0]*size for i in range(5)]
lsty0=[[0]*size for i in range(5)]
lstz0=[[0]*size for i in range(5)]
lstt0=[0]*size
print(len(lstu[0]))
for i in range(size):
    lstt0[i]=float(lstt[i][0])
    for j in range(5):
        lstx0[j][i]=float(lstx[j][i])
        lsty0[j][i]=float(lsty[j][i])
        lstz0[j][i]=float(lstz[j][i])
def graph(Fx,Fy,Fz,i):
    global lstt0
    fig=plt.figure(figsize=(18,4))
    #fig=plt.figure(figsize=(18,6))
    plt.plot(lstt0,Fx,color="r",label="Fx"+str(i+1))
    plt.plot(lstt0,Fy,color="b",label="Fy"+str(i+1))
    plt.plot(lstt0,Fz,color="y",label="Fz"+str(i+1))
    for k in range(len(lstu[0])):
        plt.vlines(x=lstt0[int(lstu[0][k])],ymin=-30,ymax=70,color="black")
    plt.xlim(0,14.5)
    plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',borderaxespad=0,fontsize=18)
    plt.ylim(-20,70)
    #plt.xlabel("time[s]",fontsize=18)
    plt.ylabel("Force[N]",fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.subplots_adjust(right=0.85)
    fig.savefig("F"+str(i+1)+".svg")
    plt.show()
for i in range(5):
    graph(lstx0[i],lsty0[i],lstz0[i],i)
'''
#jd=[[50,69],[76,94],[104,123],[132,154],[164,182],[191,214],[224,242],[250,272],[282,304]]
jd=[[40,62],[74,94],[104,125],[133,155],[163,179],[186,207],[217,239],[247,264],[276,396]]
per=[0]*8
for i in range(8):
    per[i]=lst2[jd[i+1][0]]-lst2[jd[i][0]]
print(statistics.mean(per))
print(statistics.stdev(per))
na=int(len(jd))
Sx=[0]*5
for i in range(na):
    for j in range(jd[i][0],jd[i][1]):
        Sx[0]+=Fx[0][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/(na*(jd[i][1]-jd[i][0]))
        Sx[1]+=Fx[1][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/(na*(jd[i][1]-jd[i][0]))
        Sx[2]+=Fx[2][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/(na*(jd[i][1]-jd[i][0]))
        Sx[3]+=Fx[3][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/(na*(jd[i][1]-jd[i][0]))
        Sx[4]+=Fx[4][j]*(lst2[jd[i][1]]-lst2[jd[i][0]])/(na*(jd[i][1]-jd[i][0]))
print(Sx)
with open('impulse_x.csv','w',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Sx)
            '''