class torque:
    def __init__(self, long, place, size, direction):
        self.long = long
        self.place = place
        self.size = size
        self.orientation = direction  # 逆时针为1，逆时针为-1

    def check(self):
        if self.place > self.long or self.place < 0:
            return False
        else:
            return True
