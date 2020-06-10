"""
Note that some variables used in this file are defined in boot.py
and both this files are read by ESP32 as one
"""

gps = 'NO DATA'


def wifi_connect(wifi_ssid='', wifi_pwd=''):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_ssid, wifi_pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def core_frequency_get():
    frequency = str(machine.freq()/10 ** 6)
    return 'Core frequency: ' + frequency + ' MHz'


def mcu_temperature_get():
    temp_c = str(round((esp32.raw_temperature() - 32) / 1.8, 1))
    return 'MCU temp: ' + temp_c + ' °C'


def create_index_response(connection, filename='index.html', content_type='text/html'):

    response = get_file(filename)
    response = response.format(
        gps='no data',
        frequency=core_frequency_get(),
        temperature=mcu_temperature_get(),
        dir_content=os.listdir()
    )
    connection.send('HTTP/1.1 200 OK\n')  # TODO write a cycle to send response page
    connection.send('Content-Type: ' + content_type + '\n')
    connection.send('Connection: close\n\n')
    connection.write(response)
    connection.close()


def get_file(filename):
    try:
        filesystem = os.listdir()
        if filename not in filesystem:
            error = 'Error: ' + filename + ' file not found in root dir. Found: ' + filesystem
            print(error)
            return error
        file = open(filename)
        f = file.read()
        file.close()
        return f
    except Exception as e:
        return e


def create_response(connection, filename='index.html', content_type='text/html'):
    response = get_file(filename)
    connection.send('HTTP/1.1 200 OK\n')  # TODO write a cycle to send response page
    connection.send('Content-Type: ' + content_type + '\n')
    connection.send('Connection: close\n\n')
    connection.write(response)
    connection.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


# SETUP
def setup():
    wifi_connect(WIFI_SSID, WIFI_PWD)
    gps = 'no gps data'


#  PROGRAM EXECUTION
setup()

# LOOP
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    if request.find('GET /style.css', 2, 17) >= 0:
        create_response(conn, 'style.css', 'text/css')
    elif request.find('GET /functions.js', 2, 20) >= 0:
        create_response(conn, 'functions.js', 'text/javascript')
    else:
        create_index_response(conn, 'index.html', 'text/html')
