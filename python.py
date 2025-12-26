import pyglet
from pyglet import window
from pyglet.window import key
from pyglet.window import mouse
import clan
from clan import Cletka
num_cletka_coords = (0, 0)
def num_coords():
    pass

window = pyglet.window.Window(300, 400)

baza = [Cletka(0, 0, 0), Cletka(0, 0, 16)]

@window.event
def on_draw():
    window.clear()
    baza[0].sprite_obj.draw()
    baza[1].sprite_obj.draw()
pyglet.app.run()