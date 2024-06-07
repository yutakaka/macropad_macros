# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Mac Desktop', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6600CC, 'Dock', [Keycode.COMMAND, Keycode.LEFT_ALT, Keycode.D]),
        (0x000020, 'HOME', [Keycode.HOME]),
        (0x202000, 'PgUp', [Keycode.PAGE_UP]),
        # 2nd row ----------
        (0x800000, 'DEL', [Keycode.DELETE]),
        (0x000020, 'Speak', [Keycode.SHIFT, Keycode.CONTROL, Keycode.S]),
        (0x202000, 'PgDn', [Keycode.PAGE_DOWN]),
        # 3rd row ----------
        (0x006699, 'PrevApp', [Keycode.COMMAND, Keycode.LEFT_SHIFT,Keycode.TAB]),
        (0xee6600, '^', [Keycode.CONTROL, Keycode.UP_ARROW]),
        (0x004000, 'NextApp', [Keycode.COMMAND,Keycode.TAB]),
        # 4th row ----------
        (0x202020, '<WSpace', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0xee6600, 'AppWin', [Keycode.CONTROL, Keycode.DOWN_ARROW]),
        (0x202020, 'WSpace>', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.ESCAPE])
    ]
}
