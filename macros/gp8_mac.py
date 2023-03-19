# MACROPAD Hotkeys: YouTube Browser Playback

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Guitar Pro 8 Mac', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'INS', [Keycode.INSERT]),
        (0x000020, 'Semi-', [Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.DOWN_ARROW]),
        (0x000020, 'Semi+', [Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.UP_ARROW]),      #
        # 2nd row ----------
        (0x202000, 'Rest', [Keycode.MINUS]),
        (0x202020, 'Str+', [Keycode.LEFT_ALT, Keycode.UP_ARROW]),
        (0x004000, 'Beat', [Keycode.ENTER]),
        # 3rd row ----------
        (0x202020, '<-', [Keycode.LEFT_ARROW]), # 
        (0x202020, 'Str-', [Keycode.LEFT_ALT, Keycode.DOWN_ARROW]),
        (0x202020, '->', [Keycode.RIGHT_ARROW]), # 
        # 4th row ----------
        (0x800000, '<<', [Keycode.COMMAND, Keycode.LEFT_ARROW]),   #
        (0xee6600, 'Play/Pause', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '>>', [Keycode.COMMAND, Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.F11]) # Close window/tab
    ]
}
