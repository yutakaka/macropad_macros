# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Apple Notes', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'Title', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.T]),
        (0x202000, 'Head', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.H]),
        (0x202000, 'SubHead', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.J]),
        # 2nd row ----------
        (0x202000, 'Body', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.B]),
        (0x202000, 'Mono', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.M]),
        (0x202000, '* ...', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.7]),
        # 3rd row ----------
        (0x202000, '- ...', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.8]),
        (0x202000, '1.2.3. ', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.9]),
        (0x202000, 'BQuote', [Keycode.COMMAND, Keycode.QUOTE]),
        # 4th row ----------
        (0x004000, 'Link', [Keycode.COMMAND, Keycode.K]),
        (0x101010, 'ToDo', [Keycode.LEFT_SHIFT, Keycode.COMMAND, Keycode.L]),
        (0x800000, 'Table', [Keycode.ALT, Keycode.COMMAND, Keycode.T]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
