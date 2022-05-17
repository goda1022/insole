import pandas as pd
import matplotlib.pyplot as plt
dfa=pd.read_csv('data20220428_011946.csv', header=None)#生データ取得
dfa=dfa[[0,9,10,11,12,1,2,3,4,13,14,15,16,5,6,7,8,17,18,19,20]]
print(dfa)
columns1=['sensor1_x','sensor1_y','sensor1_z','sensor2_x','sensor2_y','sensor2_z','sensor3_x','sensor3_y','sensor3_z','sensor4_x','sensor4_y','sensor4_z','sensor5_x','sensor5_y','sensor5_z',]
df=pd.DataFrame(columns=columns1)
#x,y,z方向のインダクタンスを求める
df['sensor1_x']=dfa[11]+dfa[12]-dfa[9]-dfa[10]
df['sensor1_y']=dfa[10]+dfa[11]-dfa[9]-dfa[12]
df['sensor1_z']=dfa[9]+dfa[10]+dfa[11]+dfa[12]
df['sensor2_x']=dfa[2]+dfa[3]-dfa[1]-dfa[4]
df['sensor2_y']=dfa[1]+dfa[2]-dfa[3]-dfa[4]
df['sensor2_z']=dfa[1]+dfa[2]+dfa[3]+dfa[4]
df['sensor3_x']=dfa[15]+dfa[16]-dfa[13]-dfa[14]
df['sensor3_y']=dfa[14]+dfa[15]-dfa[13]-dfa[16]
df['sensor3_z']=dfa[13]+dfa[14]+dfa[15]+dfa[16]
df['sensor4_x']=dfa[5]+dfa[8]-dfa[6]-dfa[7]
df['sensor4_y']=dfa[7]+dfa[8]-dfa[5]-dfa[6]
df['sensor4_z']=dfa[5]+dfa[6]+dfa[7]+dfa[8]
df['sensor5_x']=dfa[17]+dfa[18]-dfa[19]-dfa[20]
df['sensor5_y']=dfa[17]+dfa[20]-dfa[18]-dfa[19]
df['sensor5_z']=dfa[17]+dfa[18]+dfa[19]+dfa[20]
#初期値からの変化量を求める
df-=[df['sensor1_x'][0],df['sensor1_y'][0],df['sensor1_z'][0],df['sensor2_x'][0],df['sensor2_y'][0],df['sensor2_z'][0],df['sensor3_x'][0],df['sensor3_y'][0],df['sensor3_z'][0],df['sensor4_x'][0],df['sensor4_y'][0],df['sensor4_z'][0],df['sensor5_x'][0],df['sensor5_y'][0],df['sensor5_z'][0]]
#df=[df['sensor1_x']*0.3424,df['sensor1_y']*0.3523,df['sensor1_z']*0.4824,df['sensor2_x']*0.3416,df['sensor2_y']*0.3344,df['sensor2_z']*47.3/69,df['sensor3_x']*0.3354,df['sensor3_y']*0.3707,df['sensor3_z']*40.3/73.9,df['sensor4_x']*0.3964,df['sensor4_y']*0.3780,df['sensor4_z']*39.9/91.9,df['sensor5_x']*0.2644,df['sensor5_y']*0.2875,df['sensor5_z']*45.9/89.1]
#df.plot()
#plt.show()
df.to_csv('data_all.csv')
