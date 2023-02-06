import logging

import arcade

logger = logging.getLogger("textscreen")


class ScreenView(arcade.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self):
        pass

    def on_show_view(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
