class torque:
    def __init__(self, long, place, size, direction):
        self.long = long
        self.place = place
        self.size = size
        self.direction = direction  # 逆时针为1，顺时针为-1，向上为2，向下为-2

    def check(self):
        if self.place > self.long or self.place < 0:
            return False
        else:
            return True
