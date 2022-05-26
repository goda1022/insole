import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv
import pandas as pd
data='data20220510_122922'
# 始点(x, y, z)の座標を指定
x=[0.5,2.4,-2,-1.4,0]
y=[11.3,7.1,4,-2.3,-10.3]
df=pd.read_csv('data_all_'+data+'.csv')
size=len(df.index)
del df['time']
#for i in range(size):

# 各次元の変化量を指定

    # for i in range(5):
    # u[i],v[i],w[i]=i,i,i
# 矢印プロットを作成
#u=v=np.zeros(5)
col=["b","g","r","c","y"]
fig = plt.figure(figsize=(8, 8)) # 図の設定
ax = fig.add_subplot(111)# 3Dプロットの設定
def plot(f):
    ax.cla()
    ax.set_xlabel('x') # x軸ラベル
    ax.set_ylabel('y') # y軸ラベル
    ax.set_title(str(round((f/size),3))+"/1.00", fontsize=15) # タイトル
    #ax.legend() # 凡例
    ax.set_xlim(-25, 25) # x軸の表示範囲
    ax.set_ylim(-25, 25) # y軸の表示範囲

    # for i in range(5):
    #     u[i]=float(df.at[''[i][f])
    #     v[i]=float(df.at[[i][f])
    #     w[i]=-float(df.at[[i][f])
    #     print(u[i],df.at[''[i][f],f)
    ax.quiver(x[0], y[0], float(df.at[f,'1x']), float(df.at[f,'1y']),  color=col[0], angles='xy', scale_units='xy', scale=1)
    ax.quiver(x[1], y[1], float(df.at[f,'2x']), float(df.at[f,'2y']),  color=col[1], angles='xy', scale_units='xy', scale=1)
    ax.quiver(x[2], y[2], float(df.at[f,'3x']), float(df.at[f,'3y']),  color=col[2], angles='xy', scale_units='xy', scale=1)
    ax.quiver(x[3], y[3], float(df.at[f,'4x']), float(df.at[f,'4y']),  color=col[3], angles='xy', scale_units='xy', scale=1)
    ax.quiver(x[4], y[4], float(df.at[f,'5x']), float(df.at[f,'5y']),  color=col[4], angles='xy', scale_units='xy', scale=1) # 矢印プロット
    #ax.scatter(x, y, label='(x, y)',s=5) # 始点
    ax.scatter(x[0] , y[0] , label='(x+u, y+v, z+w)',s=5*abs(float(df.at[f,'1z']))+1,color=col[0]) # 終点
    ax.scatter(x[1] , y[1] , label='(x+u, y+v, z+w)',s=5*abs(float(df.at[f,'2z']))+1,color=col[1])
    ax.scatter(x[2] , y[2] , label='(x+u, y+v, z+w)',s=5*abs(float(df.at[f,'3z']))+1,color=col[2])
    ax.scatter(x[3] , y[3] , label='(x+u, y+v, z+w)',s=5*abs(float(df.at[f,'4z']))+1,color=col[3])
    ax.scatter(x[4] , y[4] , label='(x+u, y+v, z+w)',s=5*abs(float(df.at[f,'5z']))+1,color=col[4])
    #print(f)
        
    

    
    
anim = FuncAnimation(fig, plot,frames=size, interval=10)

anim.save('2D'+data+'.gif', writer="pillow")
plt.show()
quit()

