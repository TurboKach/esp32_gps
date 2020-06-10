# esp32_gps
MicroPython ESP32 with GPS module

# Getting started
1. Get the latest stable MicroPython [firmware](https://micropython.org/download/esp32/)  or take mine
2. Install [esptool](https://github.com/espressif/esptool)
3. Erase flash with esptool: `esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`  
4. Deploy firmware : `esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin
`  
5. Load project files to the board using [ampy](https://github.com/scientifichackers/ampy) (from project directory):  
`ampy -p /dev/tty.SLAB_USBtoUART put boot.py boot.py`  
`ampy -p /dev/tty.SLAB_USBtoUART put main.py main.py`  
`ampy -p /dev/tty.SLAB_USBtoUART put index.html index.html`  
`ampy -p /dev/tty.SLAB_USBtoUART put functions.js functions.js`  
`ampy -p /dev/tty.SLAB_USBtoUART put style.css style.css`  
6. Check it works by visiting ESP32 IP address  
7. 