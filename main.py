from pcapfile import savefile
import struct
import matplotlib.pyplot as plt
import sys
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii


##long ones 627,635


class packet():
    def __init__(self, key, packet, sep):
        self.key = key
        self.t = packet[0:2]
        if 14433 in struct.unpack("H", packet[0:2]):
            self.source = "server"
        else:
            # print(type(struct.unpack("H", packet[0:2])[0]))
            self.source = "me"
        temp = packet[76:80]
        hx = str(temp)[2:6]
        self.len = int(hx, base=16)
        self.data = packet[84:]

        tmpString = str(self.data)[4:]

        self.dataStr = tmpString[:-1]
        l = len(self.dataStr)
        r = int(l / 2)
        pretty = " "

        self.user = self.data[22:26]
        self.x = self.data[32:34]
        # print(f'{self.x} \n {self.data}')  # {self.y}')
        self.x = str(self.x)[2:]
        self.x = self.x[:-1]
        self.y = self.data[36:38]
        self.y = str(self.y)[2:]
        self.y = self.y[:-1]


        self.mouseX = self.data[40:42]
        self.mouseX = str(self.mouseX)[2:]
        self.mouseX = self.mouseX[:-1]
        self.mouseY = self.data[44:46]
        self.mouseY = str(self.mouseY)[2:]
        self.mouseY = self.mouseY[:-1]
        # print(self.mouseY)
        self.mouseXInt = int(self.mouseX, base=16)
        self.mouseYInt = int(self.mouseY, base=16)

        self.xInt = int(self.x, base=16)
        self.yInt = int(self.y, base=16)



        sepLine = 0

        for i in range(r):
            if sepLine == sep:
                pretty += "| "
                sepLine = 0
            ind = i * 2
            pretty += str(int(self.dataStr[ind:ind + 2],base=16))
            pretty += " "
            sepLine += 1
        if l % 2 != 0:
            pretty += self.dataStr[-1:-3]
        else:
            pretty = str(self.data)[2:4] + pretty
        self.pretty = pretty
        self.whole = packet


testcap = open('len23.pcap', 'rb')
capfile = savefile.load_savefile(testcap, verbose=True)


def getstart(packet):
    return packet.key


PL = len(capfile.packets)
packetDataArray = []
packetRawArray = []
for i in range(PL):
    if len(str(capfile.packets[i].packet)) == 133:
        packetDataArray.append(packet(i, capfile.packets[i].packet, 2))
# print(len(packetDataArray))
packetDataArray.sort(key=getstart)
packetsLen = len(packetDataArray)


# print(packetDataArray)

def fitTheSpace(str, l):
    while len(str) != l:
        if l - len(str) >= 2:
            str = " " + str
        str = str + " "
    return str


print('Key |  Source  |    User    |       X       |       Y       ')

# for i in range(packetsLen):
#     p = packetDataArray[i]
#     # print(f'{p.key} {p.source} {p.len} {p.data} {p.key}  ')
#     if p.source == "me":
#         print('----|----------|------------|---------------|---------------')
#         print(f'{fitTheSpace(str(p.key), 4)}|{fitTheSpace(str(p.source), 10)}|{fitTheSpace(str(p.user), 12)}|{fitTheSpace(str(p.xInt), 14)}|{fitTheSpace(str(p.yInt), 14)}')
x =[]
y=[]
mouseX=[]
mouseY=[]

#for i in range(600):
for i in range(packetsLen):
    p = packetDataArray[i]
        # print(f'{p.key} {p.source} {p.len} {p.data} {p.key}  ')
    if i % 300 == 0:
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    if p.user==b'c010':#  or 1==1:
        print('---------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------')
        print(f'{p.pretty}')#print(f'{fitTheSpace(str(p.key), 4)}|{fitTheSpace(str(p.source), 10)}|{fitTheSpace(str(p.user), 12)}|{fitTheSpace(str(p.x), 14)} |{fitTheSpace(str(p.y), 14)}')

        x.append(int(p.xInt))
        y.append(int(p.yInt))
        mouseX.append(p.mouseXInt)
        mouseY.append(p.mouseYInt)
    # print(p.whole) bca51135feb4a85e45cea08208004500002b450d000040110000c0a801242d216a93e1ec5607001759a9
    # print(p.whole) print(f'{p.source} {p.two} {p.three} {
    # p.len} {p.four} {p.space} {p.five} {
    # p.six} {p.seven} {p.eight} {p.nine} {
    # p.ten} {p.key}  ')
rows=3
cols=3
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# print(x)
# print(y)
# plt.plot(x)
# plt.xlabel('x')
# plt.show()
# plt.plot(y)
# plt.ylabel('y')
# plt.show()
# plt.plot(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# plt.plot(mouseX)
# plt.xlabel('mouseY')
# plt.show()
# plt.plot(mouseY)
# plt.xlabel('mouseY')
# plt.show()
# plt.plot(x)
# plt.plot(mouseX)
# plt.xlabel('x')
# plt.ylabel('mouseX')
# plt.show()
# plt.plot(y)
# plt.plot(mouseY)
# plt.xlabel('y')
# plt.ylabel('mouseY')
# plt.show()
#
