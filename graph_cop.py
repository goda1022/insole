import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np

with open("data_z.csv")as f:
    lst=list(csv.reader(f))
with open("data_xxx.csv")as f:
    lstx=list(csv.reader(f))
with open("data_yyy.csv")as f:
    lsty=list(csv.reader(f))
print("1")
size=int(len(lst)/5)
Fz=[[0]*size for i in range(5)]
pxyz=[[0]*size for i in range(3)]
r=[113,74.9,44.7,26.9,103]
for i in range(4):
    r[i+1]/r[0]
r[0]=1
th=[87.5,71.3,116.6,238.7,270]
FM=[0]*size
for i in range(size):
    Fz[0][i]=(int(lst[i*5][0])-int(lst[0][0]))
    Fz[1][i]=(int(lst[i*5][1])-int(lst[0][1]))
    Fz[2][i]=(int(lst[i*5][2])-int(lst[0][2]))
    Fz[3][i]=(int(lst[i*5][3])-int(lst[0][3]))
    Fz[4][i]=(int(lst[i*5][4])-int(lst[0][4]))
    #for j in range(5):
        #lstx[i][j]=int(lstx[i][j])
       # lsty[i][j]=int(lsty[i][j])
for i in range(0,size):
    if(Fz[0][i]+Fz[1][i]+Fz[2][i]+Fz[3][i]+Fz[4][i]==0):
        pxyz[0][i]=0
        pxyz[1][i]=0
        pxyz[2][i]=0
    else:
        pxyz[0][i]=(Fz[0][i]*r[0]*np.cos(np.radians(th[0]))+Fz[1][i]*r[1]*np.cos(np.radians(th[1]))+Fz[2][i]*r[2]*np.cos(np.radians(th[2]))+Fz[3][i]*r[3]*np.cos(np.radians(th[3]))+Fz[4][i]*r[4]*np.cos(np.radians(th[4])))/(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i])
        pxyz[1][i]=(Fz[0][i]*r[0]*np.sin(np.radians(th[0]))+Fz[1][i]*r[1]*np.sin(np.radians(th[1]))+Fz[2][i]*r[2]*np.sin(np.radians(th[2]))+Fz[3][i]*r[3]*np.sin(np.radians(th[3]))+Fz[4][i]*r[4]*np.sin(np.radians(th[4])))/(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i])
        #pxyz[2][i]=lstx[0]
    #with open('data_cop.csv','a',newline="")as f:
       # writer = csv.writer(f)
       # writer.writerow(pxyz[0][i],pxyz[1][i])
fig=plt.figure()    
plt.title("cop")
plt.scatter(pxyz[0],pxyz[1])
plt.plot(pxyz[0],pxyz[1])
#plt.xlim(-1.0,1.0)
#plt.ylim(-2.0,2.0)
fig.savefig("cop.png")
plt.show()
print(r)

