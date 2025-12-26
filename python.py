import pyglet
from pyglet import window
from pyglet.window import key
from pyglet.window import mouse
import clan
from clan import Cletka

batch = pyglet.graphics.Batch()
num_cletka_coords = [0, 0]
window = pyglet.window.Window(512, 512)

def num_coords() -> list:
    num_cletka_coords[0] += 16
    return num_cletka_coords

baza = []

def balj():
    for i in range(1024):
        baza.append(Cletka(0, num_coords()[0]))

def word():
    for i in range(len(baza)):
        baza[i].sprite_obj.draw()


@window.event
def on_draw():
    window.clear()
    word()
pyglet.app.run()