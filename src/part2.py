import math
import cairocffi as cairo


class Ball:

    def __init__(self, w, h, color, color_text):
        self.w = w
        self.h = h
        self.x = self.w * 0.75
        self.y = self.h * 0.20
        self.color = color[0] / 255, color[1] / 255, color[2] / 255
        self.radius = self.w * 0.16
        self.color_text = color_text[0] / 255, color_text[1] / 255, color_text[2] / 255

    def draw(self, context: cairo.Context, t):
        context.arc(self.x, self.y, self.radius, 0, 2 * math.pi)
        context.set_source_rgb(*self.color)
        context.fill()
        context.rectangle(self.x - 25, self.y - self.radius - 31, 50, 33)
        context.set_source_rgb(0, 0, 0)
        context.fill()
        context.rectangle(self.x - 2, 0, 5, self.y - self.radius)
        context.set_source_rgb(0, 0, 0)
        context.fill()
        context.set_source_rgb(*self.color_text)
        context.select_font_face("Nugie Romantic")
        context.set_font_size(150)
        size = context.text_extents("7")
        context.move_to(self.x - size[2] / 2, self.y * 0.95)
        context.show_text("7")
        context.set_font_size(50)
        size = context.text_extents("Decembre".upper())
        context.move_to(self.x - size[2] / 2, self.y * 1.2)
        context.show_text("Decembre".upper())


class CadeauTexte:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.x = self.w * 0.35
        self.y = self.h * 0.15

    def draw(self, context: cairo.Context, t):
        context.set_source_rgb(1, 1, 1)
        context.select_font_face("Nugie Romantic")
        context.set_font_size(125)
        size = context.text_extents("Un jeu")
        context.move_to(self.x - size[2] / 2, self.y * 0.95)
        context.show_text("Un jeu")
        size = context.text_extents("a boire")
        context.move_to(self.x - size[2] / 2, self.y * 0.95 + size[3] * 1.5)
        context.show_text("a boire")


class Flocon:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.flocons = [
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (- w * 0.05, - h * 0.01),
                "times": [0, 3.3, 3.7, 5, 5.4, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.75, - h * 0.01),
                "times": [0, 3.9, 4.3, 5.4, 6, -1],
                "index": 0,
                "state": 0,
            },
            {
                "image": cairo.ImageSurface.create_from_png("res/Flocon/flocon-de-neige.png"),
                "position": (w * 0.83, h * 0.45),
                "times": [0, 3.5, 4.1, 5.4, 5.8, -1],
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


class CadeauImage:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.image1 = cairo.ImageSurface.create_from_png("res/images/07/jeu-a-boire-fleche.png")
        self.image2 = cairo.ImageSurface.create_from_png("res/images/07/jeu-a-boire-fleche.png")

        img_height = self.image1.get_height()
        img_width = self.image1.get_width()
        width_ratio = float(self.w) / float(img_width)
        height_ratio = float(self.h) / float(img_height)
        self.scale1 = min(width_ratio, height_ratio) * 5 / 7
        img_height = self.image2.get_height()
        img_width = self.image2.get_width()
        width_ratio = float(self.w) / float(img_width)
        height_ratio = float(self.h) / float(img_height)
        self.scale2 = min(width_ratio, height_ratio) * 5 / 7


    def draw(self, context: cairo.Context, t):
        context.save()
        context.translate(self.w * 0.05, self.h * 0.25)
        context.rotate(0.2)
        context.scale(self.scale1, self.scale1)
        context.set_source_surface(self.image1)
        context.paint()
        context.restore()
        context.save()
        context.translate(self.w * 0.35, self.h * 0.65)
        context.rotate(-0.2)
        context.scale(self.scale2, self.scale2)
        context.set_source_surface(self.image2)
        context.paint()
        context.restore()
