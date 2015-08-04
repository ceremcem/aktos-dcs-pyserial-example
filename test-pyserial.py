__author__ = 'ceremcem'

from aktos_dcs import *
import serial


class SerialPortReader(Actor):

    def __init__(self, device_name='/dev/ttyUSB0'):
        Actor.__init__(self)

        self.ser = serial.Serial()

        self.ser.port = device_name
        self.ser.baudrate = 9600
        self.ser.bytesize = 8
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 0

        print self.ser
        try:
            self.ser.open()
        except serial.SerialException, e:
            print 'event:error\n' + 'data:' + 'Serial port error({0}): {1}\n\n'.format(e.errno, e.strerror)

    def action(self):
        print "started reading serial port..."
        try:

            str_list = []
            while True:
                sleep(0.01) # amount of time between packages
                nextchar = self.ser.read(self.ser.inWaiting())
                if nextchar:
                    str_list.append(nextchar)
                else:
                    if len(str_list) > 0:
                        print 'data:' + ''.join(str_list) + '\n\n'
                        self.send(SerialPortMessage(data=''.join(str_list)))
                        str_list = []

        except:
            print "PROBLEM!"
            pass


class TestActor(Actor):
    def handle_SerialPortMessage(self, msg):
        print "test got serial port data: ", msg.data


if __name__ == "__main__":
    SerialPortReader('/dev/pts/13')
    TestActor()

    wait_all()