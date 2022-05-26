import pandas as pd
import matplotlib.pyplot as plt
data='data20220510_151713'
waru=1
def pic(a,xs,xl,ys,yl,w):
    global data
    global df
    global waru
    #fig=plt.figure()
    # ax = fig.add_subplot(111)
    #plt.xlim([xs,xl])
    #fig=plt.figure(figsize=(12, 8))
    # plt.ylim([ys,yl])
    # plt.plot(df[a])
    # ax = fig.add_subplot(111)
    #ax.tick_params(direction = “in”, labelsize = 14)
    df.plot(y=a,ylim=[ys,yl])
    plt.savefig(w+str(waru)+'graph'+'_'+data+'.svg')
    plt.show()
dfa=pd.read_csv(data+'.csv', header=None)
#dfa=dfa[[0,9,10,11,12,1,2,3,4,13,14,15,16,5,6,7,8,17,18,19,20]]
df=pd.DataFrame()
df['time']=dfa[0]
df['1x']=dfa[11]+dfa[12]-dfa[9]-dfa[10]
df['1y']=dfa[10]+dfa[11]-dfa[9]-dfa[12]
df['1z']=dfa[9]+dfa[10]+dfa[11]+dfa[12]
df['2x']=dfa[2]+dfa[3]-dfa[1]-dfa[4]
df['2y']=dfa[1]+dfa[2]-dfa[3]-dfa[4]
df['2z']=dfa[1]+dfa[2]+dfa[3]+dfa[4]
df['3x']=dfa[15]+dfa[16]-dfa[13]-dfa[14]
df['3y']=dfa[14]+dfa[15]-dfa[13]-dfa[16]
df['3z']=dfa[13]+dfa[14]+dfa[15]+dfa[16]
df['4x']=dfa[5]+dfa[8]-dfa[6]-dfa[7]
df['4y']=dfa[7]+dfa[8]-dfa[5]-dfa[6]
df['4z']=dfa[5]+dfa[6]+dfa[7]+dfa[8]
df['5x']=dfa[17]+dfa[18]-dfa[19]-dfa[20]
df['5y']=dfa[17]+dfa[20]-dfa[18]-dfa[19]
df['5z']=dfa[17]+dfa[18]+dfa[19]+dfa[20]
print(df)
df-=[df['time'][0],df['1x'][0],df['1y'][0],df['1z'][0],df['2x'][0],df['2y'][0],df['2z'][0],df['3x'][0],df['3y'][0],df['3z'][0],df['4x'][0],df['4y'][0],df['4z'][0],df['5x'][0],df['5y'][0],df['5z'][0]]
#print(df)
df*=[0.001,0.3424,0.3523,0.4824,0.3416,0.3344,0.6855,0.3354,0.3707,0.5453,0.3964,0.3780,0.4342,0.2644,0.2875,0.5152]
#df.index=df['time']
df=df[df['time'].shift(1)!=df['time']]
df.to_csv('data_all_'+data+'.csv')
#df=df.reset_index()
df=df.iloc[:len(df.index)//waru,:]
#del df['time']
#df[['1x','1y','1z','2x','2y','2z','3x','3y','3z','4x','4y','4z','5x','5y','5z']].plot()
#df[['1z','2z','3z','4z','5z']].plot()
#df[['1x','2x','3x','4x','5x']].plot()
pic(['1x','2x','3x','4x','5x'],0,500,-25,25,'x')
pic(['1y','2y','3y','4y','5y'],0,1000,-25,25,'y')
pic(['1z','2z','3z','4z','5z'],0,1000,-10,100,'z')
print(df)
