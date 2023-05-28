# To handle the cfg file reading so a Linux / Windows user can activate the program
#
# .. program lines ....
config.read ('CPyS.cfg')
linuxport = config['DEFAULT']['linux_port']
windowsport = config['DEFAULT']['windows_port']
baud_rate = config['DEFAULT']['baudrate']
system = config['DEFAULT']['system']
autodetect = config['DEFAULT']['auto_detect']
boardnumber = config['DEFAULT']['board']

if system ==  'linux':
    com_port = linuxport
if system ==  'windows':
    com_port = windowsport
# ... program lines .....
try:
    sp = serial.Serial (port = com_port, baudrate = baud_rate,
                       bytesize = 8, timeout = 0.1, stopbits = serial.STOPBITS_ONE)
    print (com_port + ' Connected.')
except:
    print ('Comport error. No connetion for ' + com_port)
    print ('Check "CPyS.cfg" file.')
    time.sleep (5)
    sys.exit (1)
# ... rest of program ....    
