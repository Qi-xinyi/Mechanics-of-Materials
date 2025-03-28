class force:
    def __init__(self, long, place, size, direction):
        self.long = long
        self.size = size
        self.direction = direction
        self.place = place

    def check(self):
        if self.place > self.long or self.place < 0:
            return False
        else:
            return True


class force_continued:
    def __init__(self, long, place_start, place_end, size, direction):
        self.long = long
        self.size = size
        self.direction = direction  # 1为向上，2为向下
        self.place_start = place_start
        self.place_end = place_end

    def check(self):
        if self.place_end > self.long or self.place_start < 0:
            return False
        else:
            return True
