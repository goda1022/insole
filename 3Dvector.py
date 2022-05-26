import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import csv
# 始点(x, y, z)の座標を指定
x, y, z = 0, 0, 0
with open("data_xxx.csv")as f:
    lstx=list(csv.reader(f))
with open("data_yyy.csv")as f:
    lsty=list(csv.reader(f))
with open("data_zzz.csv")as f:
    lstz=list(csv.reader(f))
size=len(lstz[0])//2
# 各次元の変化量を指定
u=[0]*size
v=[0]*size
w=[0]*size
    # for i in range(5):
    # u[i],v[i],w[i]=i,i,i
artists = []
# 矢印プロットを作成

fig = plt.figure(figsize=(8, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3Dプロットの設定
def plot(u,v,w,)
    u[i]=float(lstx[4][i])
    v[i]=float(lsty[4][i])
    w[i]=-float(lstz[4][i])
    a0=ax.quiver(x, y, z, u[i], v[i], w[i], arrow_length_ratio=0.1) # 矢印プロット
    a1=ax.scatter(x, y, z, label='(x, y, z)') # 始点
    a3=ax.scatter(x + u[i], y + v[i], z + w[i], label='(x+u, y+v, z+w)') # 終点
    a4=ax.set_xlabel('x') # x軸ラベル
    a5=ax.set_ylabel('y') # y軸ラベル
    a6=ax.set_zlabel('z') # z軸ラベル
    a7=ax.set_title('quiver(x, y, z, u, v, w)', fontsize=20) # タイトル
    a8=ax.legend() # 凡例
    #a9=ax.set_xlim(0, 5) # x軸の表示範囲
    # a10=ax.set_ylim(0, 5) # y軸の表示範囲
    # a11=ax.set_zlim(0, 5) # z軸の表示範囲
    artists.append([a0,a1,a3,a4,a5,a6,a7,a8])#,a10,a11])
anim = ArtistAnimation(fig, artists)
plt.show()