
class user():
    def __init__(self, uid, packet):
        self.id = uid
        self.packets = [packet]
        self.x = [packet.x]
        self.xInt = [packet.xInt]
        self.y = [packet.y]
        self.yInt = [packet.yInt]
        self.mouseX = [packet.mouseX]
        self.mouseXInt = [packet.mouseXInt]
        self.mouseY = [packet.mouseY]
        self.mouseYInt = [packet.mouseYInt]
        self.len = 1

    def addCoords(self, packet):
        self.packets.append(packet)
        self.x.append(packet.x)
        self.xInt.append(packet.xInt)
        self.y.append(packet.y)
        self.yInt.append(packet.yInt)
        self.mouseX.append(packet.mouseX)
        self.mouseXInt.append(packet.mouseXInt)
        self.mouseY.append(packet.mouseY)
        self.mouseYInt.append(packet.mouseYInt)
        self.len = self.len + 1

    # region get functions
    def getY(self):
        return self.y

    def getYInt(self):
        return self.yInt

    def getX(self):
        return self.x

    def getXInt(self):
        return self.xInt

    def getMouseY(self):
        return self.mouseY

    def getMouseYInt(self):
        return self.mouseYInt

    def getMouseX(self):
        return self.mouseX

    def getMouseXInt(self):
        return self.mouseXInt
    # endregion
