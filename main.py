import numpy as np
import moviepy.editor as mpy
import cairocffi as cairo
import src.part as part
import src.part1 as part1
import src.part2 as part2
import src.part3 as part3

W,H = 1080, 1920
DURATION = 1

elements = [
    [
        part.Background(W, H, (10, 47, 99)),
        part1.Ball(W, H, (134, 185, 255), (5, 2, 1)),
        part.Kraken(W, H),
        part1.Flocon(W, H),
    ],
    [
        part.Background(W, H, (10, 47, 99)),
        part2.Ball(W, H, (134, 185, 255), (5, 2, 1)),
        part2.CadeauImage(W, H),
        part2.CadeauTexte(W, H),
        part.Kraken(W, H),
        part2.Flocon(W, H),
    ],
    [
        part.Background(W, H, (10, 47, 99)),
        part3.Kraken(W, H),
        part3.Ball(W, H, (134, 185, 255), (5, 2, 1)),
        part3.Gagnant(W, H, (21, 121, 255)),
        part3.Flocon(W, H),
    ],
]


def make_frame(t):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    context = cairo.Context(surface)
    # for element in elements[2]:
    for element in elements[int(t * len(elements) / DURATION)]:
        element.draw(context, t)

    im = 0 + np.frombuffer(surface.get_data(), np.uint8)
    im.shape = (surface.get_height(), surface.get_width(), 4)
    im = im[:, :, [2, 1, 0, 3]]
    return im

clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("tombola.gif",fps=1, opt="OptimizePlus")
