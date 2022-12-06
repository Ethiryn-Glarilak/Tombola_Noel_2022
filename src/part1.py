import math
import cairocffi as cairo


class Ball:

    def __init__(self, w, h, color, color_text):
        self.w = w
        self.h = h
        self.x = w / 2 + w / 48
        self.y = h / 2 - h / 48
        self.color = color[0] / 255, color[1] / 255, color[2] / 255
        self.radius = w * 0.75 / 2
        self.color_text = color_text[0] / 255, color_text[1] / 255, color_text[2] / 255

    def draw(self, context: cairo.Context, t):
        context.arc(self.x, self.y, self.radius, 0, 2 * math.pi)
        context.set_source_rgb(*self.color)
        context.fill()
        context.rectangle(self.x - 75, self.y - self.radius - 90, 150, 100)
        context.set_source_rgb(0, 0, 0)
        context.fill()
        context.rectangle(self.x - 10, 0, 25, self.y - self.radius)
        context.set_source_rgb(0, 0, 0)
        context.fill()
        context.set_source_rgb(*self.color_text)
        context.select_font_face("Nugie Romantic")
        context.set_font_size(400)
        size = context.text_extents("7")
        context.move_to(self.x - size[2] / 2, self.y + self.h * 0.05)
        context.show_text("7")
        context.set_font_size(100)
        size = context.text_extents("Decembre".upper())
        context.move_to(self.x - size[2] / 2, self.y + self.h * 0.13)
        context.show_text("Decembre".upper())


class Flocon:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.flocons = [
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.10, - h * 0.01),
                "times": [0, 0.1, 0.5, 1.4, 1.8, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (- w * 0.01, h * 0.18),
                "times": [0, 0.7, 1.1, 2, 2.4, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.83, h * 0.10),
                "times": [0, 0.5, 0.9, 1.8, 2.2, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (- w * 0.10, h * 0.55),
                "times": [0, 0.9, 1.3, 2.2, 2.6, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.60, h * 0.63),
                "times": [0, 1.1, 1.5, 2.4, 2.8, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.80, h * 0.86),
                "times": [0, 1.2, 1.6, 2.5, 2.9, -1],
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
