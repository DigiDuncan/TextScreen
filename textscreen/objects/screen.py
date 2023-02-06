import arcade
import arcade.text
from arcade.sections import Section

class TextScreen(Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, name = "TextScreen",
            accept_keyboard_keys = True, accept_mouse_events = True, local_mouse_coordinates = True, **kwargs)

        self.text_lines = []
        self.font_size = 16

        self.screen_width: int = 40
        self.screen_height: int = 20

    def calculate_screen(self):
        test_character = arcade.text.Text("a", 0, 0,
            font_size = self.font_size, font_name = "FiraCode Nerd Font Mono",
            anchor_x = "left", anchor_y = "top")

        self.screen_width = self.width // test_character.content_width
        self.screen_height = self.height // test_character.content_height

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)
