import pyglet

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
    sprite_obj = pyglet.sprite.Sprite(sprite[1])
    def __init__(self, number: int, x: int, y: int):
        self.number = number
        self.x = x
        self.y = y
