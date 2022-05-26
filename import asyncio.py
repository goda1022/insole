import asyncio
from bleak import BleakClient
import time
import msvcrt
import os
import datetime

now = datetime.datetime.now()

# ここだけ変える
MAC_ADDRESS = ("94:B9:7E:AB:7F:D6")
SAVE_FILE_PATH = "data" + now.strftime('%Y%m%d_%H%M%S') + ".csv"
# mac address
# M5StickC-Plus1 94:B9:7E:AB:7F:D6
# insole_M5_1 94:B9:7E:AB:7F:66
# insole_fether D0:07:0E:96:D1:37

# ファイルのある場所で実行する
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 設計パラメータ
BYTE_HEADER1 = b'\x00'
BYTE_HEADER2 = b'\x11'
NOTIFY_CHARACTERISTIC_UUID = ("a8a5068c-a6f7-d44d-2c89-e77c8bd8aaba")
RESET_CHARACTERISTIC_UUID = ("1a6912b7-5d9e-123f-d35d-91df992a2fc0")
SENSOR_OFFSET = 2000
SENS_NUM = 5

inductance = [[0] *4 for i in range(5)]
byte_catch_flag1 = False
byte_catch_flag2 = False
thread_flag = True
count = 0
count_test = 0
start_time = time.perf_counter()
timestamp_data = 0

def data_converter(sender, data):
    global byte_catch_flag1
    global byte_catch_flag2
    global count
    global count_test
    global f
    global timestamp_data

    count_test += 1
    byte_array = [0] * 20
    for i in range(20):
        byte_array[i] = data[i:i+1]

    if byte_array[0] == BYTE_HEADER1:
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

    if byte_array[0] == BYTE_HEADER2:
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

        # タイムスタンプの確認
        timestamp1 = int.from_bytes(byte_array[15], byteorder='big', signed=False)
        timestamp2 = int.from_bytes(byte_array[16], byteorder='big', signed=False)
        timestamp3 = int.from_bytes(byte_array[17], byteorder='big', signed=False)
        timestamp4 = int.from_bytes(byte_array[18], byteorder='big', signed=False)
        print(timestamp1, timestamp2, timestamp3, timestamp4)
        timestamp_data = ((timestamp1 << 24) | (timestamp2 << 16) | (timestamp3 << 8) | timestamp4)
        print(timestamp_data)

    if byte_catch_flag1 and byte_catch_flag2:
        byte_catch_flag1 = False
        byte_catch_flag2 = False
        # print(inductance)
        data_str = ",".join(map(str,[x for row in inductance for x in row]))
        f.write(str(timestamp_data) + "," + data_str + "\n")
        count += 1

async def stop_ble_notify(client, uuid):
    await client.stop_notify(uuid)
    print("BLE notify stopped.")

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        x = await client.is_connected()
        print("Connected: {0}".format(x))

        await client.start_notify(NOTIFY_CHARACTERISTIC_UUID, data_converter)
        #await asyncio.sleep(10)
        await key_wait()
        # await loop_inf()
        await stop_ble_notify(client, NOTIFY_CHARACTERISTIC_UUID)

async def key_wait():
    while True:
        await asyncio.sleep(0.01)
        if msvcrt.kbhit():
            return

if __name__ == "__main__":
    f = open(SAVE_FILE_PATH, mode="w")

    address = MAC_ADDRESS
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop))
    print(count)
    # print(count_test)

    f.close()