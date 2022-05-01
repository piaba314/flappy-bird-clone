class Animation:
    def __init__(self, images, time):
        self.images = images
        self.time = time
        self.image = self.images[0]
        self.image_index = 0
        self.ticks = 0

    def update(self, delta):
        self.ticks += delta
        if self.ticks >= self.time:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.ticks = 0
