import smbus
import time

class MLX90614():

    MLX90614_TA    = 0x06
    MLX90614_TOBJ1 = 0x07

    def __init__(self, address = 0x5a, bus = 1):
        self.address = address
        self.bus = smbus.SMBus(bus)

    def readValue(self, registerAddress):
        error = None
        for i in range(3):
            try:
                return self.bus.read_word_data(self.address, registerAddress)
            except IOError as e:
                error = e
                sleep(0.1)
        raise error

    def valueToCelcius(self, value):
        return -273.15 + (value * 0.02)

    def readObjectTemperature(self):
        value = self.readValue(self.MLX90614_TOBJ1)
        return self.valueToCelcius(value)

    def readAmbientTemperature(self):
        value = self.readValue(self.MLX90614_TA)
        return self.valueToCelcius(value)
