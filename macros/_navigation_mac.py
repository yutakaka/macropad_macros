# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'nav-Mac', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6600CC, 'VolUp', [ConsumerControlCode.VOLUME_INCREMENT]),
        (0x000020, 'HOME', [Keycode.HOME]),
        (0x202000, 'PgUp', [Keycode.PAGE_UP]),
        # 2nd row ----------
        (0x6600CC, 'VolDn', [ConsumerControlCode.VOLUME_DECREMENT]),
        (0x000020, 'END', [Keycode.END]),
        (0x202000, 'PgDn', [Keycode.PAGE_DOWN]),
        # 3rd row ----------
        (0x006699, 'ESC', [Keycode.ESCAPE]),
        (0x202020, '', [Keycode.UP_ARROW]),
        (0x004000, 'Enter', [Keycode.ENTER]),
        # 4th row ----------
        (0x202020, '<WSpace', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0xee6600, '^', [Keycode.CONTROL, Keycode.UP_ARROW]),
        (0x202020, 'WSpace>', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.ESCAPE])
    ]
}
