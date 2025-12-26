import pyglet
import python
sprite = [pyglet.image.load('ass/default.png'),
            pyglet.image.load('ass/empty0.png'),
            pyglet.image.load('ass/empty1.png'),
            pyglet.image.load('ass/empty2.png'),
            pyglet.image.load('ass/empty3.png'),
            pyglet.image.load('ass/empty4.png'),
            pyglet.image.load('ass/empty5.png'),
            pyglet.image.load('ass/empty6.png'),
            pyglet.image.load('ass/empty7.png'),
            pyglet.image.load('ass/empty8.png')]

class Cletka:
    mina = False
    number = None
    x = None
    y = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite_obj = pyglet.sprite.Sprite(sprite[0], x=self.x, y=self.y, batch=python.batch)