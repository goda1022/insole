import asyncio
from bleak import BleakClient
import msvcrt
import time
import csv
import numpy as np
from playsound import playsound
import pygame.mixer


CHAR_UUID  = ("a8a5068c-a6f7-d44d-2c89-e77c8bd8aaba")
RESET_CHARACTERISTIC_UUID = ("1a6912b7-5d9e-123f-d35d-91df992a2fc0")
SENSOR_OFFSET = 2000
SENS_NUM = 5

inductance = [[0] *4 for i in range(5)]
byte_catch_flag1 = False
byte_catch_flag2 = False
thread_flag = True
count = 0
count2=time.time()
count3=0
BLE_count = 0
Fz = [0]*5
Fz2 = [0]*5
Fx = [[0]*2 for i in range(SENS_NUM)]
Fyy=[0]*SENS_NUM
Fxx=[0]*SENS_NUM
first=0
ut=[0]*2
iti=0
#while(1):
#playsound("C:\\Users\\Fellowship\\okk.mp3")


def data_converter(sender, data):
    global byte_catch_flag1
    global byte_catch_flag2
    global count
    global count2
    global BLE_count
    global Fz
    global Fz2
    global Fx
    global Fyy
    global Fxx
    global ut
    global first
    global iti
    BLE_count += 1
    byte_array = [0] * 20
    for i in range(20):
        byte_array[i] = data[i:i+1]

    if byte_array[0] == b'\x01':
        for i in range(3):
            for j in range(4):
                if j == 0:
                    data_top = int.from_bytes(byte_array[1 + 6*i], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*i + 1], byteorder='big', signed=False)
                    inductance[i][j] = ((data_top << 4) | (data_bottom >> 4)) + SENSOR_OFFSET
                elif j == 1:
                    data_top = int.from_bytes(byte_array[1 + 6*i + 1], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*i + 2], byteorder='big', signed=False)
                    inductance[i][j] = (((data_top & 0b00001111) << 8) | data_bottom) + SENSOR_OFFSET
                elif j == 2:
                    data_top = int.from_bytes(byte_array[1 + 6*i + 3], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*i + 4], byteorder='big', signed=False)
                    inductance[i][j] = ((data_top << 4) | (data_bottom >> 4)) + SENSOR_OFFSET
                elif j == 3:
                    data_top = int.from_bytes(byte_array[1 + 6*i + 4], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*i + 5], byteorder='big', signed=False)
                    inductance[i][j] = (((data_top & 0b00001111) << 8) | data_bottom) + SENSOR_OFFSET
        byte_catch_flag1 = True
        ut[0]=time.time()
        

    if byte_array[0] == b'\x10':
        for i in range(3,SENS_NUM):
            for j in range(4):
                if j == 0:
                    data_top = int.from_bytes(byte_array[1 + 6*(i-3)], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*(i-3) + 1], byteorder='big', signed=False)
                    inductance[i][j] = ((data_top << 4) | (data_bottom >> 4)) + SENSOR_OFFSET
                elif j == 1:
                    data_top = int.from_bytes(byte_array[1 + 6*(i-3) + 1], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*(i-3) + 2], byteorder='big', signed=False)
                    inductance[i][j] = (((data_top & 0b00001111) << 8) | data_bottom) + SENSOR_OFFSET
                elif j == 2:
                    data_top = int.from_bytes(byte_array[1 + 6*(i-3) + 3], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*(i-3) + 4], byteorder='big', signed=False)
                    inductance[i][j] = ((data_top << 4) | (data_bottom >> 4)) + SENSOR_OFFSET
                elif j == 3:
                    data_top = int.from_bytes(byte_array[1 + 6*(i-3) + 4], byteorder='big', signed=False)
                    data_bottom = int.from_bytes(byte_array[1 + 6*(i-3) + 5], byteorder='big', signed=False)
                    inductance[i][j] = (((data_top & 0b00001111) << 8) | data_bottom) + SENSOR_OFFSET
        byte_catch_flag2 = True
        ut[0]=time.time()
        

    if byte_catch_flag1 and byte_catch_flag2:
        byte_catch_flag1 = False
        byte_catch_flag2 = False
        if first==0 and ut[0]!=0:
            ut[1]=ut[0]
            first=1
        if(count%5==0):
            
            print(inductance)
            #print(count2)
            #print(ut)
            ut[0]-=ut[1]
            with open('data_time.csv','a',newline="")as f:
                writer = csv.writer(f)
                writer.writerow(ut)
        with open('data_all.csv','a',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(inductance)

        count += 1
        #Fzを求める
        for i in range(SENS_NUM):
            for j in range(4):
                Fz[i]+=inductance[i][j]
        #並び替え
        Fz2[0]=Fz[2]
        Fz2[1]=Fz[0]
        Fz2[2]=Fz[3]
        Fz2[3]=Fz[1]
        Fz2[4]=Fz[4]
       
        #せんだん力を求める
        Fx[0][0]=inductance[2][2]+inductance[2][3]-inductance[2][1]-inductance[2][0]
        Fx[0][1]=inductance[2][2]+inductance[2][1]-inductance[2][3]-inductance[2][0]
        Fx[1][0]=inductance[0][2]+inductance[0][1]-inductance[0][3]-inductance[0][0]#lx
        #Fx[1][0]=-(inductance[0][2]+inductance[0][1]-inductance[0][3]-inductance[0][0])#rx
        Fx[1][1]=inductance[0][0]+inductance[0][1]-inductance[0][3]-inductance[0][2]#ly
        #Fx[1][1]=-(Fx[1][1])#ry
        Fx[2][0]=inductance[3][2]+inductance[3][3]-inductance[3][1]-inductance[3][0]
        Fx[2][1]=inductance[3][2]+inductance[3][1]-inductance[3][3]-inductance[3][0]
        Fx[3][0]=inductance[1][0]+inductance[1][3]-inductance[1][1]-inductance[1][2]#lx
        #Fx[3][0]=-(inductance[1][0]+inductance[1][3]-inductance[1][1]-inductance[1][2])#Rx
        Fx[3][1]=inductance[1][2]+inductance[1][3]-inductance[1][0]-inductance[1][1]#ly
        #Fx[3][1]=-(inductance[1][2]+inductance[1][3]-inductance[1][0]-inductance[1][1])#ry
        Fx[4][0]=inductance[4][0]+inductance[4][1]-inductance[4][2]-inductance[4][3]
        Fx[4][1]=inductance[4][0]+inductance[4][3]-inductance[4][1]-inductance[4][2]
        #せんだん力をまとめる
        for i in range(SENS_NUM):
            Fxx[i]=Fx[i][0]
        if iti==0:
            iti=Fx[4][0]
        
            #count2=time.time()
        for i in range(SENS_NUM):
            Fyy[i]=Fx[i][1]
        with open('data_z.csv','a',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Fz2)
        #Fzを初期化
        for j in range(SENS_NUM):
            Fz[j] = 0
        with open('data_y.csv','a',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Fyy)
        with open('data_x.csv','a',newline="")as f:
            writer = csv.writer(f)
            writer.writerow(Fxx)
        
async def stop_ble_notify(client, uuid):
    await client.stop_notify(uuid)
    print("BLE notify stopped.")

async def run(loop):
    async with BleakClient(address, loop=loop) as client:
        print("Subscribing to characteristic changes...")
        await client.start_notify(CHAR_UUID, data_converter)
        
        #await sound()
        # await loop_inf()
        #await asyncio.sleep(10)
        #await key_wait()
        await stop_ble_notify(client, CHAR_UUID)
        
# async def sound():
#     global count3
#     while True:
#         await asyncio.sleep(0.01)
#         if (Fx[4][0]-iti)*0.2664-0.0977>-3.0:
#                 count3=0
#         elif (Fx[4][0]-iti)*0.2664-0.0977<-3.0 and (Fx[4][0]-iti)*0.2664-0.0977>=-5:
#             if count3>10:
#                 count3=0
#                 pygame.mixer.init() #初期化
#                 pygame.mixer.music.load("sei2.mp3") #読み込み
#                 pygame.mixer.music.play(1) #再生
#                 await asyncio.sleep(1)
#                 pygame.mixer.music.stop() #終了
#             else:
#                 count3+=1
#         if (Fx[4][0]-iti)*0.2664-0.0977<-5:
#             count3=0
#             pygame.mixer.init() #初期化
#             pygame.mixer.music.load("ok.mp3") #読み込み
#             pygame.mixer.music.play(1) #再生
#             await asyncio.sleep(1)
#             pygame.mixer.music.stop() #終了
#         if msvcrt.kbhit():
#             return
async def loop_inf():
    while True:
        await asyncio.sleep(10)

async def key_wait():
    while True:
        await asyncio.sleep(0.01)
        if msvcrt.kbhit():
            return

if __name__ == "__main__":
    # mac address
    # M5StickC-Plus1 
    address=("94:B9:7E:AB:7F:D6")
    #address = ("94:B9:7E:AB:7F:66")#left
    #address = ("94:B9:7E:92:4A:5E")#right
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address))
    print(count)
    print(BLE_count)