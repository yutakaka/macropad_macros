# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'tmux', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6600CC, 'Ctr+B', [Keycode.CONTROL, Keycode.B]),
        (0x000020, 'Pane+', [Keycode.LEFT_ALT, Keycode.UP_ARROW]),
        (0x202000, 'ScrlU', [Keycode.PAGE_UP]),
        # 2nd row ----------
        (0x800000, 'Quit', [Keycode.Q]),
        (0x000020, 'Pane=', [Keycode.LEFT_ALT, Keycode.DOWN_ARROW]),
        (0x202000, 'ScrlD', [Keycode.PAGE_DOWN]),
        # 3rd row ----------
        (0x006699, 'Prev', [Keycode.P]),
        (0xee6600, 'Up', [Keycode.UP_ARROW]),
        (0x004000, 'Next', [Keycode.N]),
        # 4th row ----------
        (0xee6600, 'Left', [Keycode.LEFT_ARROW]),
        (0xee6600, 'Down', [Keycode.DOWN_ARROW]),
        (0xee6600, 'Right', [Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.Z]) # Zoom in/out
    ]
}
