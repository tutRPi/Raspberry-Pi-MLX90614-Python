from MLX90614 import *

if __name__ == "__main__":
    sensor = MLX90614()
    print("Object:", sensor.readObjectTemperature())
    print("Ambient:", sensor.readAmbientTemperature())
