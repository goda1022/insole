import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.animation as anm

with open("data_z.csv")as f:
    lst=list(csv.reader(f))

size=int(len(lst)/5)
Fz1=[0]*size
Fz2=[0]*size
Fz3=[0]*size
Fz4=[0]*size
Fz5=[0]*size
px=[0]*size
py=[0]*size
r1=113
r2=74.9/r1
r3=44.7/r1
r4=26.9/r1
r5=103/r1
r1=1
for i in range(size):
    Fz1[i]=(int(lst[i*5][0])-int(lst[0][0]))/100
    Fz2[i]=(int(lst[i*5][1])-int(lst[0][1]))/100
    Fz3[i]=(int(lst[i*5][2])-int(lst[0][2]))/100
    Fz4[i]=(int(lst[i*5][3])-int(lst[0][3]))/100
    Fz5[i]=(int(lst[i*5][4])-int(lst[0][4]))/100

for i in range(0,size):
    if(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i]==0):
        px[i]=0
        py[i]=0
    else:
        #px[i]=(Fz1[i]*113*np.sin(87.5)+Fz2[i]*74.9*np.sin(71.3)+Fz3[i]*44.7*np.sin(116.6)+Fz4[i]*26.9*np.sin(238.7)+Fz5[i]*10.3*np.sin(270))/(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i])
        #py[i]=(Fz1[i]*113*np.cos(87.5)+Fz2[i]*74.9*np.cos(71.3)+Fz3[i]*44.7*np.cos(116.6)+Fz4[i]*26.9*np.cos(238.7)+Fz5[i]*10.3*np.cos(270))/(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i])
        px[i]=(Fz1[i]*r1*np.cos(np.radians(87.5))+Fz2[i]*r2*np.cos(np.radians(71.3))+Fz3[i]*r3*np.cos(np.radians(116.6))+Fz4[i]*r4*np.cos(np.radians(238.7))+Fz5[i]*r5*np.cos(np.radians(270)))#/(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i])#left
        py[i]=(Fz1[i]*r1*np.sin(np.radians(87.5))+Fz2[i]*r2*np.sin(np.radians(71.3))+Fz3[i]*r3*np.sin(np.radians(116.6))+Fz4[i]*r4*np.sin(np.radians(238.7))+Fz5[i]*r5*np.sin(np.radians(270)))#/(Fz1[i]+Fz2[i]+Fz3[i]+Fz4[i]+Fz5[i])#left
fig=plt.figure(figsize=(5,10))    
'''
anim=[]
tt=np.arange(0,size,1)

for i in tt:
    im=plt.plot(px[i],py[i])
    anim.append(im)
anim=animation.ArtistAnimation(fig,anim)
plt.title("cop")
plt.xlim(-1.0,1.0)
plt.ylim(-2.0,2.0)'''
def update(i,fig_title,A):
    if i!=0:
        plt.cla()
    plt.plot(px[i],py[i],"r",marker='.')
    plt.title(fig_title+', i='+str(i))
    plt.xlim(-1.0,1.0)
    plt.ylim(-2.0,2.0)
ani=anm.FuncAnimation(fig,update,fargs=('cop',2),interval=70,frames=size)
ani.save("cop_animation.gif",writer='imagemagick')

