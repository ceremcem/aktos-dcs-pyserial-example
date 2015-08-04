# Dependencies:

1. [aktos_dcs](https://github.com/ceremcem/aktos-dcs)
2. PySerial: `sudo easy_install pyserial`

# Usage

1. Setup your serial ports:

    1. If you have real serial port adaptor(s):
        Connect these adaptor(s)

    2. If you want to use virtual serial port pair:

            $ socat -d -d pty,raw,echo=0 pty,raw,echo=0

        above command will output something like:

            ceremcem@cca-erik:~$ socat -d -d pty,raw,echo=0 pty,raw,echo=0
            2015/08/03 23:42:40 socat[31540] N PTY is /dev/pts/13
            2015/08/03 23:42:40 socat[31540] N PTY is /dev/pts/15
            2015/08/03 23:42:40 socat[31540] N starting data transfer loop with FDs [5,5] and [7,7]

        Then use `/dev/pts/13` and `/dev/pts/15` as your virtual serial port pairs.



    Get the port pair's names. Lets say these are '/dev/PORT_A' and '/dev/PORT_B'.

2. Open `/dev/PORT_A` with your favourite serial port application (mine is CuteCom)

3. Open `/dev/PORT_B` with the serial port application in a new window.

4. Type "hello" from window 1, verify that you will see this message from window 2. Else, you didn't
   setup your serial ports correctly. Fix this issue.

5. Close window 2, so `/dev/PORT_B` becomes free.

6. Edit `test-pyserial.py` and change the line from `SerialPortReader('/dev/pts/13')` to
    `SerialPortReader('/dev/PORT_B')`.

7. Run the test application: `python test-pyserial.py`

8. Switch to window 1 (the one you opened `/dev/PORT_A`) and type "hello", click send.