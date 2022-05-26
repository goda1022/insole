import numpy as np
import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.animation as anm

with open("data_xxx.csv")as f:
    lst=list(csv.reader(f))
with open("data_yyy.csv")as f:
    lst1=list(csv.reader(f))
size=int(len(lst[0]))
for i in range(size):
    for j in range(5):
        lst[j][i]=int(lst[j][i])
        lst1[j][i]=int(lst1[j][i])
print(size)
# 5×5サイズのFigureを作成してAxesを追加
fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)  

def update(i,fig_title,A):
    if i!=0:
        plt.cla()
    # 格子点を表示
    ax.grid()
# 軸ラベルの設定
    ax.set_xlabel("x", fontsize = 16)
    ax.set_ylabel("y", fontsize = 16)
# 軸範囲の設定
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
# x軸とy軸
    ax.axhline(0, color = "gray")
    ax.axvline(0, color = "gray")
# ベクトルを表示
# quiver(始点x,始点y,終点x,終点y)
    ax.quiver(0, 0, lst[4][i], lst1[4][i], color = "red",
          angles = 'xy', scale_units = 'xy', scale = 1)
# ベクトルにテキストを添える
    #ax.text(2, 1, "[2, 1]", color = "red", size = 15)
ani=anm.FuncAnimation(fig,update,fargs=('cop',2),interval=70,frames=size)
ani.save("vector.gif",writer='imagemagick')


