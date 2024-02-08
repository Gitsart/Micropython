import machine
import time

uart = machine.UART(2, baudrate=9600, tx=17, rx=16)  # Specify UART2, TX on GPIO 17, RX on GPIO 16

def send_data(data):
    uart.write(data)

while True:
    send_data("Hello from ESP32!\n")
    time.sleep(2)
