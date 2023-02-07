import logging
from turtle import Vec2D

import arcade
import arcade.key
from arcade.experimental.crt_filter import CRTFilter

from textscreen.objects.screen import TextScreen

logger = logging.getLogger("textscreen")


class ScreenView(arcade.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        window = arcade.get_window()
        self.section = TextScreen(0, 0, window.width, window.height)
        self.section.enabled = True
        self.section_manager.add_section(self.section)

        self.crt_filter = CRTFilter(window.width, window.height,
                            resolution_down_scale=1.0,
                            hard_scan=-8.0,
                            hard_pix=-3.0,
                            display_warp = Vec2D(1.0 / 32.0, 1.0 / 18.0),
                            mask_dark=0.5,
                            mask_light=1.5)
        self.filter_on = True

    def setup(self):
        pass

    def on_show_view(self):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        print(f"wanted {arcade.key.F} and modifiers to be & 2, got {symbol} and {modifiers} ({modifiers & 2})")
        if symbol == arcade.key.F and modifiers & arcade.key.MOD_CTRL:
            self.filter_on = not self.filter_on

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
