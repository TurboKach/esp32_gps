# esp32_gps
MicroPython ESP32 with GPS module

# Getting started
1. Get the latest stable MicroPython [firmware](https://micropython.org/download/esp32/)  or take mine
2. Install [esptool](https://github.com/espressif/esptool)
3. Erase flash with esptool: `esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`  
4. Deploy firmware : `esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin
`  
5. 