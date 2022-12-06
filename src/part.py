import cairocffi as cairo

class Background:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color[0] / 255, color[1] / 255, color[2] / 255

    def draw(self, context: cairo.Context, t):
        context.rectangle(0, 0, self.width, self.height)
        context.set_source_rgb(*self.color)
        context.fill()


class Kraken:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.kraken = cairo.ImageSurface.create_from_png("res/kraken_noel_logo.png")
        img_height = self.kraken.get_height()
        img_width = self.kraken.get_width()
        width_ratio = float(self.w) / float(img_width)
        height_ratio = float(self.h) / float(img_height)
        self.scale = min(width_ratio, height_ratio) * 2 / 3
        self.x = - w * 3 / 32
        self.y = h * 2 / 3

    def draw(self, context: cairo.Context, t):
        context.save()
        context.translate(self.x, self.y)
        context.scale(self.scale, self.scale)
        context.set_source_surface(self.kraken)
        context.paint()
        context.restore()
