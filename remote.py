from socket import socket, AF_INET, SOCK_STREAM
import binascii
import time



def sendCommand(input):
    text = str(input)

    if text == '1':
        data = binascii.unhexlify(r'1f30413109')
    elif text == '2':
        data = binascii.unhexlify(r'1f30413209')
    elif text == '3':
        data = binascii.unhexlify(r'1f30413309')
    elif text == '4':
        data = binascii.unhexlify(r'1f30413409')
    elif text == '5':
        data = binascii.unhexlify(r'1f30413509')
    elif text == '6':
        data = binascii.unhexlify(r'1f30413609')
    elif text == '7':
        data = binascii.unhexlify(r'1f30413709')
    elif text == '8':
        data = binascii.unhexlify(r'1f30413809')
    elif text == '9':
        data = binascii.unhexlify(r'1f30413909')
    elif text == '0':
        data = binascii.unhexlify(r'1f30413009')
    elif text == 'power':
        data = binascii.unhexlify(r'1f30414509')
    elif text == "edit":
        data = binascii.unhexlify(r'1f30414609')
    elif text == 'set':
        data = binascii.unhexlify(r'1f30414709')
    elif text == 'wrc':
        data = binascii.unhexlify(r'1f30414a09')
    elif text == 'cyc':
        data = binascii.unhexlify(r'1f30414a09')
    elif text == 'left':
        data = binascii.unhexlify(r'1f30414809')
    elif text == 'right':
        data = binascii.unhexlify(r'1f30414909')
    elif text == 'clock':
        data = binascii.unhexlify(r'1f30414b09')
    elif text == 'up':
        data = binascii.unhexlify(r'1f30414c09')
    elif text == 'down':
        data = binascii.unhexlify(r'1f30414d09')
    elif text == 'enter':
        data = binascii.unhexlify(r'1f30415209')
    elif text == 'stopwatch':
        data = binascii.unhexlify(r'1f30414e09')
    elif text == 'reset':
        data = binascii.unhexlify(r'1f30414f09')
    elif text == 'stop':
        data = binascii.unhexlify(r'1f30415009')
    elif text == 'start':
        data = binascii.unhexlify(r'1f30415109')
    else:
        raise ValueError('Unsupported Send Value')



    #ADDRESS = '192.168.1.100'  # connection address
    #PORT = 50000  # connection port


    #s = socket(AF_INET, SOCK_STREAM)
    #s.connect((ADDRESS, PORT))
    #s.send(data)
    time.sleep(1)
    print ("Sent " + text)




