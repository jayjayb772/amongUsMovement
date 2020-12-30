from pcapfile import savefile
import struct
from User import user
from Packet import packet
import matplotlib.pyplot as plt
import numpy
import sys
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii

##long ones 627,635

testcap = open('MovementOnlyamongUs12_1.pcap', 'rb')
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
x = []
y = []
mouseX = []
mouseY = []

temps = {}

# for i in range(600):
for i in range(packetsLen):
    p = packetDataArray[i]
    if p.user in temps:
        temps[p.user].addCoords(p)
    else:
        temps.update({p.user: user(p.user, p)})
users = {}
for u in temps:
    if temps[u].len > 100:
        users.update({temps[u].id: temps[u]})
    else:
        print(temps[u].len)
        print(temps[u].id)
        for p in temps[u].packets:
            print(p.dataStr)

# print(users)



img = plt.imread("map.png")
fig, ax = plt.subplots()
ax.imshow(img, extent=[45, 195, 69, 151])
# ax.xlim(55, 190)  # 135
# ax.ylim(70, 150)  # 90


i = 0
while i < 940:
    # for i in range(940):
    img = plt.imread("map.png")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[45, 195, 69, 151])

    for u in users:
        # print(users[u].id)
        # print(numpy.amin(users[u].getXInt()))
        # print(users[u].getYInt())
        # print(numpy.amin(users[u].getYInt()))
        # print(users[u].len)
        # print(f'{p.key} {p.source} {p.len} {p.data} {p.key}  ')
        if (len(users[u].getYInt()) > i):
            ax.plot(users[u].getXInt()[i:i + 20], users[u].getYInt()[i:i + 20])
        else:
            ax.plot(users[u].getXInt()[-30:], users[u].getYInt()[-30:])

    plt.savefig('plts/' + str(i) + '.png', bbox_inches='tight')
    plt.show()

    i += 10

plt.show()

# if p.user==b'b710'  or 1==1:
#     print('---------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------')
#     print(f'{p.pretty}')#print(f'{fitTheSpace(str(p.key), 4)}|{fitTheSpace(str(p.source), 10)}|{fitTheSpace(str(p.user), 12)}|{fitTheSpace(str(p.x), 14)} |{fitTheSpace(str(p.y), 14)}')
#
#     x.append(int(p.xInt))
#     y.append(int(p.yInt))
#     mouseX.append(p.mouseXInt)
#     mouseY.append(p.mouseYInt)


# print(p.whole) bca51135feb4a85e45cea08208004500002b450d000040110000c0a801242d216a93e1ec5607001759a9
# print(p.whole) print(f'{p.source} {p.two} {p.three} {
# p.len} {p.four} {p.space} {p.five} {
# p.six} {p.seven} {p.eight} {p.nine} {
# p.ten} {p.key}  ')


# rows=3
# cols=3
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

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
