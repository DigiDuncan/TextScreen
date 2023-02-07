import arcade
import arcade.text
from arcade.sections import Section

class TextScreen(Section):
    def __init__(self, left: int, bottom: int, width: int, height: int, **kwargs):
        super().__init__(left, bottom, width, height, name = "TextScreen",
            accept_keyboard_keys = True, accept_mouse_events = True, local_mouse_coordinates = True,
            prevent_dispatch_view = None, prevent_dispatch = None, **kwargs)

        window = arcade.get_window()

        self.text_lines = ["This is a test!"]
        self.font_size = 16

        self.screen_width: int = 40
        self.screen_height: int = 20

        self.calculate_screen()

        self.text = arcade.text.Text("\n".join(self.text_lines[-self.screen_height:]), 0, window.height,
            font_size = self.font_size, font_name = "FiraCode Nerd Font Mono",
            anchor_x = "left", anchor_y = "top", multiline = True, width = window.width)

    def calculate_screen(self):
        test_character = arcade.text.Text("a", 0, 0,
            font_size = self.font_size, font_name = "FiraCode Nerd Font Mono",
            anchor_x = "left", anchor_y = "top")

        self.screen_width = self.width // test_character.content_width
        self.screen_height = self.height // test_character.content_height

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        return super().on_key_press(symbol, modifiers)

    def on_draw(self):
        if self.view.filter_on:
            # Draw our stuff into the CRT filter instead of on screen
            self.view.crt_filter.use()
            self.view.crt_filter.clear()
            self.text.draw()

            # Next, switch back to the screen and dump the contents of the CRT filter
            # to it.
            self.view.window.use()
            self.view.clear()
            self.view.crt_filter.draw()
        else:
            self.view.window.use()
            self.view.clear()
            self.text.draw()
