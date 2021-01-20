import struct
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
