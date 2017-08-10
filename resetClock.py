import remote
import time
def reset():
    remote.sendCommand('edit')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('0')
    remote.sendCommand('enter')
    remote.sendCommand('start')
    print("Clock Has been reset!!!!!")
    time.sleep(10)
