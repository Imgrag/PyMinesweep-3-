import pyglet
from pyglet.window import key
from pyglet.window import mouse
import clan

window = pyglet.window.Window()



@window.event
def on_draw():
    window.clear()

pyglet.app.run()