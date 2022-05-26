import asyncio
from asyncio import tasks
from bleak import BleakClient
import msvcrt
import time

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from asyncqt import QEventLoop, asyncSlot

UUID  = ("a8a5068c-a6f7-d44d-2c89-e77c8bd8aaba")
RESET_CHARACTERISTIC_UUID = ("1a6912b7-5d9e-123f-d35d-91df992a2fc0")
SENSOR_OFFSET = 2000
SENS_NUM = 5
PLOT_DATA_NUM = 100

inductance = [[SENSOR_OFFSET] *4 for i in range(5)]
byte_catch_flag1 = False
byte_catch_flag2 = False
thread_flag = True
count = 0
BLE_count = 0

plot_data_num = 50

class Window(pg.GraphicsLayoutWidget):
    def __init__(self, loop=None, parent=None):
        super().__init__(parent)
        self._loop = loop

        self.setWindowTitle("pyqtgraph example: Scrolling Plots")
        plot = self.addPlot()
        self._data1 = np.zeros(plot_data_num)
        self._data2 = np.zeros(plot_data_num)
        self._data3 = np.zeros(plot_data_num)
        self._data4 = np.zeros(plot_data_num)
        self._data5 = np.zeros(plot_data_num)
        self._curve1 = plot.plot(self.data1)
        self._curve2 = plot.plot(self.data2)
        self._curve3 = plot.plot(self.data3)
        self._curve4 = plot.plot(self.data4)
        self._curve5 = plot.plot(self.data5)
        self._client = BleakClient(address, loop=self._loop)

        plot.setYRange(4100, 4700, padding=0)

    @property
    def client(self):
        return self._client

    async def start(self):
        await self.client.connect()
        await self.client.start_notify(UUID, data_converter)
        self.start_read()

    async def stop(self):
        await self.client.stop_ble_notify(self.client, UUID)
        await self.client.disconnect()

    @property
    def data1(self):
        return self._data1

    @property
    def data2(self):
        return self._data2

    @property
    def data3(self):
        return self._data3

    @property
    def data4(self):
        return self._data4

    @property
    def data5(self):
        return self._data5

    @property
    def curve1(self):
        return self._curve1

    @property
    def curve2(self):
        return self._curve2

    @property
    def curve3(self):
        return self._curve3

    @property
    def curve4(self):
        return self._curve4

    @property
    def curve5(self):
        return self._curve5

    async def read(self):
        global inductance

        inductance_data1 = (inductance[0][0] + inductance[0][1] + inductance[0][2] + inductance[0][3])/4
        inductance_data2 = (inductance[1][0] + inductance[1][1] + inductance[1][2] + inductance[1][3])/4
        inductance_data3 = (inductance[2][0] + inductance[2][1] + inductance[2][2] + inductance[2][3])/4
        inductance_data4 = (inductance[3][0] + inductance[3][1] + inductance[3][2] + inductance[3][3])/4
        inductance_data5 = (inductance[4][0] + inductance[4][1] + inductance[4][2] + inductance[4][3])/4
        try:
            plot_inductance1 = float(inductance_data1)
            plot_inductance2 = float(inductance_data2)
            plot_inductance3 = float(inductance_data3)
            plot_inductance4 = float(inductance_data4)
            plot_inductance5 = float(inductance_data5)
        except ValueError as e:
            print("Value type error. Cannot convert to float.")
        else:
            self.update_plot(plot_inductance1, plot_inductance2, plot_inductance3, plot_inductance4, plot_inductance5)
        QtCore.QTimer.singleShot(5, self.start_read)

    def start_read(self):
        asyncio.ensure_future(self.read(), loop=self._loop)

    def update_plot(self, plot_inductance1, plot_inductance2, plot_inductance3, plot_inductance4, plot_inductance5):
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = plot_inductance1
        self.curve1.setData(self.data1)
        self.data2[:-1] = self.data2[1:]
        self.data2[-1] = plot_inductance2
        self.curve2.setData(self.data2)
        self.data3[:-1] = self.data3[1:]
        self.data3[-1] = plot_inductance3
        self.curve3.setData(self.data3)
        self.data4[:-1] = self.data4[1:]
        self.data4[-1] = plot_inductance4
        self.curve4.setData(self.data4)
        self.data5[:-1] = self.data5[1:]
        self.data5[-1] = plot_inductance5
        self.curve5.setData(self.data5)

    def closeEvent(self, event):
        super().closeEvent(event)
        asyncio.ensure_future(self.client.stop(), loop=self._loop)

def data_converter(sender, data):
    global byte_catch_flag1
    global byte_catch_flag2
    global count
    global BLE_count
    global f
    global inductance

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

    if byte_catch_flag1 and byte_catch_flag2:
        byte_catch_flag1 = False
        byte_catch_flag2 = False
        print(inductance)
        count += 1
        f.write("\n")
        f.write(str(time.time()) + str(inductance) + "\n")


async def stop_ble_notify(client, uuid):
    await client.stop_notify(uuid)
    print("BLE notify stopped.")

async def loop_inf():
    while True:
        await asyncio.sleep(10)

async def key_wait():
    while True:
        await asyncio.sleep(0.01)
        if msvcrt.kbhit():
            return

def run(args):
    app = QtGui.QApplication(args)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = Window()
    window.show()

    with loop:
        asyncio.ensure_future(window.start(), loop=loop)
        loop.run_forever()

if __name__ == "__main__":
    import sys

    save_file_path = "data_M5.txt"
    f = open(save_file_path, mode="w")

    # mac address
    # M5StickC-Plus1 94:B9:7E:AB:7F:D6
    # M5StickC-Plus1 94:B9:7E:AB:7F:66
    # insole_M5_3 "94:B9:7E:93:36:FE"
    # insole_ESP32_1 "3C:61:05:4A:D9:7A"
    address = ("94:B9:7E:AB:7F:D6")
    # run(address)
    run(sys.argv)

    f.close()