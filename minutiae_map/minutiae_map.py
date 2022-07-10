class MinutiaeMap:
    def __init__(self):
        self.minutiae_list = []


class MinutiaeInformation:
    def __init__(self, x, y, theta, quality):
        self.x_position = x
        self.y_position = y
        self.theta = theta
        self.quality = quality
