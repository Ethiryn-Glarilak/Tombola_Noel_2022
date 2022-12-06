import math
import cairocffi as cairo


class Ball:

    def __init__(self, w, h, color, color_text):
        self.w = w
        self.h = h
        self.x = self.w * 0.5
        self.y = self.h * 0.25
        self.color = color[0] / 255, color[1] / 255, color[2] / 255
        self.radius = self.w * 0.2
        self.color_text = color_text[0] / 255, color_text[1] / 255, color_text[2] / 255

    def draw(self, context: cairo.Context, t):
        context.arc(self.x, self.y, self.radius, 0, 2 * math.pi)
        context.set_source_rgb(*self.color)
        context.fill()
        context.rectangle(self.x - 31, self.y - self.radius - 35, 62, 38)
        context.set_source_rgb(0, 0, 0)
        context.fill()
        context.rectangle(self.x - 3, 0, 7, self.y - self.radius)
        context.set_source_rgb(0, 0, 0)
        context.fill()
        context.set_source_rgb(*self.color_text)
        context.select_font_face("Nugie Romantic")
        context.set_font_size(175)
        size = context.text_extents("7")
        context.move_to(self.x - size[2] / 2, self.y * 0.95)
        context.show_text("7")
        context.set_font_size(62)
        size = context.text_extents("Decembre".upper())
        context.move_to(self.x - size[2] / 2, self.y * 1.2)
        context.show_text("Decembre".upper())


class Gagnant:

    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.x = self.w * 0.5
        self.y = self.h * 0.5
        self.color = color[0] / 255, color[1] / 255, color[2] / 255

    def draw(self, context: cairo.Context, t):
        # alpha = self.get_alpha(t)
        context.select_font_face("Nugie Romantic")
        context.set_font_size(125)
        size = context.text_extents("Bravo a".upper())
        context.move_to(self.x - size[2] / 2, self.y * 0.95)
        context.set_source_rgba(1, 1, 1)
        context.show_text("Bravo a".upper())
        context.set_font_size(100)
        size = context.text_extents("Clemence B.")
        context.move_to(self.x - size[2] / 2 + 5, self.y * 0.95 + 150 + 5)
        context.set_source_rgba(1, 1, 1)
        context.show_text("Clemence B.")
        context.move_to(self.x - size[2] / 2, self.y * 0.95 + 150)
        context.set_source_rgba(*self.color)
        context.show_text("Clemence B.")
        context.set_font_size(50)
        size = context.text_extents("Notre".upper())
        context.move_to(self.x - size[2] / 2, self.y * 0.95 + 150 + 150)
        context.set_source_rgba(1, 1, 1)
        context.show_text("Notre".upper())
        # context.set_font_size(50)
        size = context.text_extents("Gagnante".upper())
        context.move_to(self.x - size[2] / 2, self.y * 0.95 + 150 + 150 + 75)
        context.set_source_rgba(1, 1, 1)
        context.show_text("Gagnante".upper())


class Flocon:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.flocons = [
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (- w * 0.05, h * 0.05),
                "times": [0, 6, 6.4, 7.3, 7.7, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.68, - h * 0.02),
                "times": [0, 6.2, 6.6, 7.5, 7.9, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.72, h * 0.29),
                "times": [0, 6.4, 6.8, 7.7, 8.1, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (- w * 0.05, h * 0.45),
                "times": [0, 6.6, 7, 7.9, 8.3, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.75, h * 0.65),
                "times": [0, 6.8, 7.2, 8.1, 8.5, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (- w * 0.02, h * 0.80),
                "times": [0, 7, 7.4, 8.3, 8.7, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.80, h * 0.88),
                "times": [0, 7.2, 7.6, 8.5, 8.9, -1],
                "index": 0,
                "state": 0,
            },
        ]

    def draw(self, context: cairo.Context, t):
        for flocon in self.flocons:
            context.save()
            context.translate(*flocon.get("position"))
            context.scale(0.5, 0.5)
            context.set_source_surface(flocon.get("image"))
            context.paint_with_alpha(self.get_alpha(t, flocon))
            # context.paint()
            context.restore()

    def get_alpha(self, t, flocon):
        next_times = flocon.get("times")[flocon.get("index") + 1]
        if t > next_times and next_times != -1:
            flocon["index"] += 1
            flocon["state"] = (flocon.get("state") + 1) % 4
        actual_times = flocon.get("times")[flocon.get("index")]
        next_times = flocon.get("times")[flocon.get("index") + 1]
        state = flocon.get("state")

        if state == 0:
            return 0
        elif state == 1:
            return (t - actual_times) / (next_times - actual_times)
        elif state == 2:
            return 1
        else:
            return 1 - (t - actual_times) / (next_times - actual_times)


class Kraken:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.kraken = cairo.ImageSurface.create_from_png("res/kraken_noel_logo.png")
        img_height = self.kraken.get_height()
        img_width = self.kraken.get_width()
        width_ratio = float(self.w) / float(img_width)
        height_ratio = float(self.h) / float(img_height)
        self.scale = min(width_ratio, height_ratio) * 4 / 7
        self.x = self.w * 0.5 - img_width * 0.5 * self.scale
        self.y = self.h * 0.72

    def draw(self, context: cairo.Context, t):
        context.save()
        context.translate(self.x, self.y)
        context.scale(self.scale, self.scale)
        context.set_source_surface(self.kraken)
        context.paint()
        context.restore()
