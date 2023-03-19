# MACROPAD Hotkeys: YouTube Browser Playback

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'GP8 Edit Mode', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'INS', [Keycode.INSERT]),
        (0x000020, 'Semi-', [Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.DOWN_ARROW]),
        (0x000020, 'Semi+', [Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.UP_ARROW]),      #
        # 2nd row ----------
        (0x202000, 'Rest', [Keycode.MINUS]),
        (0x004000, 'ShortN', [Keycode.MINUS]),
        (0x004000, 'LongN', [Keycode.EQUALS]),
        # 3rd row ----------
        (0x6600CC, 'Ring', [Keycode.I]), # 
        (0x202020, 'Str+', [Keycode.LEFT_ALT, Keycode.UP_ARROW]),
        (0x6600CC, 'Tripl', [Keycode.FORWARD_SLASH]), # 
        # 4th row ----------
        (0x6600CC, 'Gliss.', [Keycode.S]),   #
        (0x202020, 'Str-', [Keycode.LEFT_ALT, Keycode.DOWN_ARROW]),   # Toggle Play/Pause
        (0x6600CC, 'Tie', [Keycode.L]), #
        # Encoder button ---
        (0x000000, '', [Keycode.F11]) # Full Screen
    ]
}
