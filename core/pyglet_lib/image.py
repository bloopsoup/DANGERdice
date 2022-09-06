import pyglet
from ..components import AbstractImage, tl_to_bl


class Border(pyglet.shapes.BorderedRectangle):
    def _update_color(self):
        opacity = int(self._opacity)
        self._vertex_list.colors[:] = [*self._rgb, 0] * 4 + [*self._brgb, opacity] * 4


class Image(AbstractImage):
    def __init__(self, image: pyglet.image):
        super().__init__(image)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.width, self.height = self.sprite.width, self.sprite.height

    def blit_border(self, pos: tuple[int, int], color: tuple[int, int, int], size: int):
        new_pos = tl_to_bl((pos[0], pos[1] + self.height), 600)
        border = Border(new_pos[0], new_pos[1], self.width, self.height, size + 2, (0, 0, 0),
                                                 (0, 0, 0))
        border.draw()

    def blit(self, pos: tuple[int, int]):
        self.sprite.position = tl_to_bl((pos[0], pos[1] + self.height), 600)
        self.sprite.draw()
